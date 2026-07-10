#!/usr/bin/env python3
"""RZ1 audit tracking API with versioned and traceable JSON responses."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
import uuid
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from typing import Any, Dict, List
from urllib.parse import parse_qs, urlparse

# Allow running from repository root or from the api/ directory.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
from compliance_mapper import compute_compliance_scores  # noqa: E402
from alert_engine import (  # noqa: E402
    load_alerts,
    process_and_store_event_alerts,
    process_and_store_risk_alerts,
)

OUTPUT_VERSION = "RZ1-1.0"
GOVERNANCE_VERSION = "1.0"
EVENT_STORE = Path("/tmp/rz1_audit_events.jsonl")


def utc_now() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat().replace("+00:00", "Z")


def make_trace_id(trace_id: str = "") -> str:
    return trace_id or str(uuid.uuid4())


def versioned_response(data: Any, trace_id: str) -> Dict[str, Any]:
    return {
        "output_version": OUTPUT_VERSION,
        "governance_version": GOVERNANCE_VERSION,
        "generated_at": utc_now(),
        "trace_id": trace_id,
        "data": data,
    }


def build_event(payload: Dict[str, Any], trace_id: str) -> Dict[str, Any]:
    return {
        "output_version": OUTPUT_VERSION,
        "governance_version": GOVERNANCE_VERSION,
        "record_type": "audit_event",
        "event_id": str(uuid.uuid4()),
        "trace_id": payload.get("trace_id") or trace_id,
        "created_at": utc_now(),
        "event": payload.get("event", "unspecified_event"),
        "actor": payload.get("actor", "api-client"),
        "status": payload.get("status", "accepted"),
        "details": payload.get("details", {}),
        "source": "api/audit_api.py",
    }


def load_events(limit: int = 50) -> List[Dict[str, Any]]:
    if not EVENT_STORE.exists():
        return []
    events: List[Dict[str, Any]] = []
    with EVENT_STORE.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            events.append(json.loads(line))
    return events[-limit:]


def load_events_since(since_ts: str) -> List[Dict[str, Any]]:
    """Return all events with created_at strictly after *since_ts* (ISO 8601)."""
    if not EVENT_STORE.exists():
        return []
    results: List[Dict[str, Any]] = []
    with EVENT_STORE.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            event = json.loads(line)
            if event.get("created_at", "") > since_ts:
                results.append(event)
    return results


def append_event(event: Dict[str, Any]) -> None:
    EVENT_STORE.parent.mkdir(parents=True, exist_ok=True)
    with EVENT_STORE.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(event) + "\n")


def compute_risk(payload: Dict[str, Any], trace_id: str, events: List[Dict[str, Any]]) -> Dict[str, Any]:
    def clamp(value: int) -> int:
        return max(1, min(5, value))

    impact = clamp(int(payload.get("impact", 3)))
    likelihood = clamp(int(payload.get("likelihood", 3)))
    detectability = clamp(int(payload.get("detectability", 3)))
    control_strength = clamp(int(payload.get("control_strength", 3)))
    score = max(1, min(100, ((impact * likelihood) + detectability - control_strength) * 5))
    if score <= 20:
        level = "low"
    elif score <= 40:
        level = "moderate"
    elif score <= 60:
        level = "high"
    elif score <= 80:
        level = "very_high"
    else:
        level = "critical"

    compliance_scores = compute_compliance_scores(events)

    return {
        "output_version": OUTPUT_VERSION,
        "governance_version": GOVERNANCE_VERSION,
        "record_type": "risk_assessment",
        "generated_at": utc_now(),
        "trace_id": trace_id,
        "inputs": {
            "impact": impact,
            "likelihood": likelihood,
            "detectability": detectability,
            "control_strength": control_strength,
        },
        "risk_score": score,
        "risk_level": level,
        "compliance": compliance_scores,
        "source": "api/audit_api.py",
    }


class AuditAPIHandler(BaseHTTPRequestHandler):
    server_version = "RZ1AuditAPI/1.0"

    def _trace_id(self) -> str:
        return make_trace_id(self.headers.get("X-Trace-Id", ""))

    def _send(self, status: int, payload: Dict[str, Any], trace_id: str) -> None:
        body = json.dumps(versioned_response(payload, trace_id), indent=2).encode("utf-8")
        header_trace_id = str(uuid.uuid4())
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("X-Trace-Id", header_trace_id)
        self.end_headers()
        self.wfile.write(body)

    def _read_json(self) -> Dict[str, Any]:
        size = int(self.headers.get("Content-Length", "0"))
        if size == 0:
            return {}
        raw = self.rfile.read(size).decode("utf-8")
        return json.loads(raw)

    def do_GET(self) -> None:  # noqa: N802
        trace_id = self._trace_id()
        parsed = urlparse(self.path)

        if parsed.path == "/health":
            self._send(HTTPStatus.OK, {"status": "ok"}, trace_id)
            return

        if parsed.path == "/version":
            self._send(
                HTTPStatus.OK,
                {
                    "api_version": OUTPUT_VERSION,
                    "governance_version": GOVERNANCE_VERSION,
                    "available_endpoints": [
                        "GET /health",
                        "GET /version",
                        "GET /audit/events?limit=50",
                        "GET /audit/events/{trace_id}",
                        "GET /audit/stream?since=<iso_timestamp>",
                        "GET /alerts?limit=100",
                        "POST /audit/events",
                        "POST /risk/score",
                    ],
                },
                trace_id,
            )
            return

        if parsed.path == "/audit/stream":
            query = parse_qs(parsed.query)
            since_ts = query.get("since", [""])[0]
            if not since_ts:
                # Default: events from the last 60 seconds
                since_ts = (
                    dt.datetime.now(dt.timezone.utc) - dt.timedelta(seconds=60)
                ).isoformat().replace("+00:00", "Z")
            new_events = load_events_since(since_ts)
            self._send(
                HTTPStatus.OK,
                {
                    "since": since_ts,
                    "server_time": utc_now(),
                    "count": len(new_events),
                    "events": new_events,
                },
                trace_id,
            )
            return

        if parsed.path == "/alerts":
            query = parse_qs(parsed.query)
            limit = int(query.get("limit", ["100"])[0])
            limit = max(1, min(500, limit))
            self._send(HTTPStatus.OK, {"alerts": load_alerts(limit)}, trace_id)
            return

        if parsed.path == "/audit/events":
            query = parse_qs(parsed.query)
            limit = int(query.get("limit", ["50"])[0])
            limit = max(1, min(200, limit))
            self._send(HTTPStatus.OK, {"events": load_events(limit)}, trace_id)
            return

        if parsed.path.startswith("/audit/events/"):
            requested_trace_id = parsed.path.rsplit("/", 1)[-1]
            events = [event for event in load_events(200) if event.get("trace_id") == requested_trace_id]
            self._send(HTTPStatus.OK, {"events": events, "count": len(events)}, trace_id)
            return

        self._send(HTTPStatus.NOT_FOUND, {"error": "not_found"}, trace_id)

    def do_POST(self) -> None:  # noqa: N802
        trace_id = self._trace_id()
        try:
            payload = self._read_json()
        except json.JSONDecodeError:
            self._send(HTTPStatus.BAD_REQUEST, {"error": "invalid_json"}, trace_id)
            return

        if self.path == "/audit/events":
            event = build_event(payload, trace_id)
            append_event(event)
            triggered_alerts = process_and_store_event_alerts(event)
            self._send(
                HTTPStatus.CREATED,
                {"event": event, "alerts_triggered": len(triggered_alerts)},
                trace_id,
            )
            return

        if self.path == "/risk/score":
            try:
                events = load_events(200)
                result = compute_risk(payload, trace_id, events)
            except ValueError:
                self._send(HTTPStatus.BAD_REQUEST, {"error": "invalid_risk_input"}, trace_id)
                return
            triggered_alerts = process_and_store_risk_alerts(result)
            self._send(
                HTTPStatus.OK,
                {"risk": result, "alerts_triggered": len(triggered_alerts)},
                trace_id,
            )
            return

        self._send(HTTPStatus.NOT_FOUND, {"error": "not_found"}, trace_id)


def run_server(host: str, port: int) -> None:
    server = HTTPServer((host, port), AuditAPIHandler)
    print(f"RZ1 audit API listening on http://{host}:{port}")
    server.serve_forever()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run RZ1 audit tracking API.")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8080)
    args = parser.parse_args()
    run_server(args.host, args.port)
