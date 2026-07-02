#!/usr/bin/env python3
"""RZ1 audit logging generator with versioned, traceable JSON output."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
import uuid
from typing import Any, Dict


def utc_now() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat().replace("+00:00", "Z")


def parse_details(details_raw: str) -> Dict[str, Any]:
    try:
        parsed = json.loads(details_raw)
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid details JSON: {exc}") from exc
    if not isinstance(parsed, dict):
        raise ValueError("details must be a JSON object")
    return parsed


def build_record(args: argparse.Namespace) -> Dict[str, Any]:
    return {
        "output_version": args.output_version,
        "governance_version": args.governance_version,
        "record_type": "audit_event",
        "event_id": str(uuid.uuid4()),
        "trace_id": args.trace_id or str(uuid.uuid4()),
        "created_at": utc_now(),
        "event": args.event,
        "actor": args.actor,
        "status": args.status,
        "source": "scripts/audit_logger.py",
        "details": parse_details(args.details),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate RZ1 JSON audit event records.")
    parser.add_argument("--event", required=True, help="Event name")
    parser.add_argument("--actor", default="system", help="Event actor")
    parser.add_argument("--status", default="ok", help="Event status")
    parser.add_argument("--details", default="{}", help="JSON object string for event details")
    parser.add_argument("--trace-id", dest="trace_id", default="", help="Optional trace identifier")
    parser.add_argument("--output-version", default="RZ1-1.0")
    parser.add_argument("--governance-version", default="1.0")
    parser.add_argument("--output", default="", help="Optional output file path")
    args = parser.parse_args()

    try:
        record = build_record(args)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 2

    payload = json.dumps(record, indent=2)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as handle:
            handle.write(payload + "\n")
    print(payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
