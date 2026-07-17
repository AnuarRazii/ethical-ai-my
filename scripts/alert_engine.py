#!/usr/bin/env python3
"""RZ1 real-time alert engine.

Evaluates audit events and risk assessments against alert thresholds and
writes triggered alerts to a separate append-only JSONL store.

Alert conditions
----------------
- risk_score_high  : risk_score > RISK_SCORE_THRESHOLD (70 on the 1-100 scale,
                     equivalent to 0.7 when normalised)
- compliance_fail  : any per-regulation compliance score < COMPLIANCE_FAIL_THRESHOLD
"""

from __future__ import annotations

import datetime as dt
import json
import uuid
from pathlib import Path
from typing import Any, Dict, List, Optional

# ---------------------------------------------------------------------------
# Thresholds
# ---------------------------------------------------------------------------

# risk_score is on the 1-100 scale used throughout audit_api.py
RISK_SCORE_THRESHOLD: int = 70

# Compliance scores are in [0, 1]; below this value counts as a failure
COMPLIANCE_FAIL_THRESHOLD: float = 0.5

# ---------------------------------------------------------------------------
# Storage
# ---------------------------------------------------------------------------

ALERT_STORE = Path("/tmp/rz1_alerts.jsonl")


def utc_now() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat().replace("+00:00", "Z")


# ---------------------------------------------------------------------------
# Alert building
# ---------------------------------------------------------------------------

def _build_alert(
    alert_type: str,
    severity: str,
    message: str,
    trace_id: str,
    details: Dict[str, Any],
) -> Dict[str, Any]:
    return {
        "record_type": "alert",
        "alert_id": str(uuid.uuid4()),
        "alert_type": alert_type,
        "severity": severity,
        "message": message,
        "trace_id": trace_id,
        "triggered_at": utc_now(),
        "details": details,
        "source": "scripts/alert_engine.py",
    }


# ---------------------------------------------------------------------------
# Store helpers
# ---------------------------------------------------------------------------

def append_alert(alert: Dict[str, Any]) -> None:
    """Append a single alert to the JSONL alert store."""
    ALERT_STORE.parent.mkdir(parents=True, exist_ok=True)
    with ALERT_STORE.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(alert) + "\n")


def load_alerts(limit: int = 100) -> List[Dict[str, Any]]:
    """Load the most recent *limit* alerts from the alert store."""
    if not ALERT_STORE.exists():
        return []
    alerts: List[Dict[str, Any]] = []
    with ALERT_STORE.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if line:
                alerts.append(json.loads(line))
    return alerts[-limit:]


# ---------------------------------------------------------------------------
# Condition evaluation
# ---------------------------------------------------------------------------

def evaluate_risk_alerts(risk_result: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Return a list of alerts triggered by *risk_result*.

    Checks:
    1. risk_score > RISK_SCORE_THRESHOLD
    2. Any compliance score < COMPLIANCE_FAIL_THRESHOLD
    """
    triggered: List[Dict[str, Any]] = []
    trace_id: str = risk_result.get("trace_id", "")
    risk_score: int = int(risk_result.get("risk_score", 0))
    risk_level: str = risk_result.get("risk_level", "unknown")
    compliance: Dict[str, float] = risk_result.get("compliance", {})

    # --- Alert 1: high risk score ---
    if risk_score > RISK_SCORE_THRESHOLD:
        alert = _build_alert(
            alert_type="risk_score_high",
            severity="high",
            message=(
                f"Risk score {risk_score} exceeds threshold {RISK_SCORE_THRESHOLD} "
                f"(level: {risk_level})"
            ),
            trace_id=trace_id,
            details={
                "risk_score": risk_score,
                "risk_level": risk_level,
                "threshold": RISK_SCORE_THRESHOLD,
            },
        )
        triggered.append(alert)

    # --- Alert 2: compliance failures ---
    failed_regs = {
        regulation: score
        for regulation, score in compliance.items()
        if score < COMPLIANCE_FAIL_THRESHOLD
    }
    if failed_regs:
        alert = _build_alert(
            alert_type="compliance_fail",
            severity="high",
            message=(
                "Compliance check failed for: "
                + ", ".join(
                    f"{reg} ({score:.4f})" for reg, score in failed_regs.items()
                )
            ),
            trace_id=trace_id,
            details={
                "failed_regulations": failed_regs,
                "threshold": COMPLIANCE_FAIL_THRESHOLD,
                "all_scores": compliance,
            },
        )
        triggered.append(alert)

    return triggered


def evaluate_event_alerts(event: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Return alerts triggered by a single audit event (status-based heuristic).

    An immediate alert fires when a known high-severity violation status is
    present so that the event streaming path can surface incidents without
    waiting for a full risk assessment.
    """
    HIGH_SEVERITY_STATUSES = {"violation", "breach", "non_compliant", "bypassed"}
    triggered: List[Dict[str, Any]] = []
    status: str = event.get("status", "")
    if status in HIGH_SEVERITY_STATUSES:
        alert = _build_alert(
            alert_type="event_violation",
            severity="high",
            message=(
                f"Audit event '{event.get('event', 'unknown')}' reported "
                f"high-severity status '{status}'"
            ),
            trace_id=event.get("trace_id", ""),
            details={
                "event_id": event.get("event_id", ""),
                "event": event.get("event", ""),
                "actor": event.get("actor", ""),
                "status": status,
            },
        )
        triggered.append(alert)
    return triggered


def process_and_store_risk_alerts(risk_result: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Evaluate *risk_result*, persist any triggered alerts, and return them."""
    alerts = evaluate_risk_alerts(risk_result)
    for alert in alerts:
        append_alert(alert)
    return alerts


def process_and_store_event_alerts(event: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Evaluate *event*, persist any triggered alerts, and return them."""
    alerts = evaluate_event_alerts(event)
    for alert in alerts:
        append_alert(alert)
    return alerts
