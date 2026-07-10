#!/usr/bin/env python3
"""RZ1 compliance mapping engine.

Maps audit events to regulatory frameworks (PDPA, GDPR, EU AI Act) and
produces a per-regulation compliance score in the range [0.0, 1.0].
"""

from __future__ import annotations

from typing import Dict, List

# ---------------------------------------------------------------------------
# Regulation definitions
# ---------------------------------------------------------------------------

# Each regulation entry lists:
#   positive_patterns  – substrings in an event name that indicate a
#                        compliance-positive action for that regulation
#   negative_patterns  – substrings that indicate a compliance-negative action
#   positive_statuses  – event status values counted as compliant
#   negative_statuses  – event status values counted as non-compliant
# ---------------------------------------------------------------------------

REGULATION_DEFINITIONS: Dict[str, Dict[str, List[str]]] = {
    "PDPA": {
        "positive_patterns": [
            "consent",
            "personal_data",
            "data_subject",
            "privacy_notice",
            "data_access",
            "data_deletion",
            "data_correction",
            "data_subject_request",
            "retention_policy",
        ],
        "negative_patterns": [
            "unauthorized_access",
            "data_breach",
            "consent_missing",
            "retention_violation",
            "unlawful_processing",
        ],
        "positive_statuses": ["ok", "accepted", "completed", "granted", "processed"],
        "negative_statuses": ["rejected", "error", "violation", "breach", "denied", "failed"],
    },
    "GDPR": {
        "positive_patterns": [
            "consent",
            "personal_data",
            "data_subject",
            "privacy_notice",
            "data_access",
            "data_deletion",
            "data_portability",
            "right_to_erasure",
            "processing_record",
            "dpia",
            "data_protection",
        ],
        "negative_patterns": [
            "unauthorized_access",
            "data_breach",
            "consent_missing",
            "retention_violation",
            "unlawful_processing",
            "cross_border_violation",
        ],
        "positive_statuses": ["ok", "accepted", "completed", "granted", "processed"],
        "negative_statuses": ["rejected", "error", "violation", "breach", "denied", "failed"],
    },
    "EU_AI_Act": {
        "positive_patterns": [
            "model",
            "ai_decision",
            "bias_check",
            "fairness",
            "explainability",
            "human_oversight",
            "risk_assessment",
            "conformity_check",
            "transparency",
            "audit_trail",
            "logging",
        ],
        "negative_patterns": [
            "bias_detected",
            "unexplained_decision",
            "oversight_bypassed",
            "non_compliant",
            "prohibited_practice",
        ],
        "positive_statuses": ["ok", "accepted", "completed", "passed", "logged"],
        "negative_statuses": [
            "rejected",
            "error",
            "violation",
            "non_compliant",
            "failed",
            "bypassed",
        ],
    },
}


def _event_matches(event_name: str, patterns: List[str]) -> bool:
    """Return True if any pattern substring appears in the event name."""
    lower = event_name.lower()
    return any(p in lower for p in patterns)


def map_event_to_regulations(event: Dict) -> List[str]:
    """Return the list of regulation keys that an audit event is relevant to."""
    event_name: str = event.get("event", "")
    matched: List[str] = []
    for regulation, defn in REGULATION_DEFINITIONS.items():
        if _event_matches(event_name, defn["positive_patterns"]) or _event_matches(
            event_name, defn["negative_patterns"]
        ):
            matched.append(regulation)
    return matched


def _score_for_regulation(events: List[Dict], regulation: str) -> float:
    """Compute a compliance score in [0.0, 1.0] for a single regulation.

    Uses Laplace-smoothed proportion of positive signals:
        score = (positives + 1) / (positives + negatives + 2)

    This ensures:
    - No events for a regulation → neutral score of 0.5
    - All positive events → approaches 1.0
    - All negative events → approaches 0.0
    """
    defn = REGULATION_DEFINITIONS[regulation]

    positives = 0
    negatives = 0

    for event in events:
        event_name: str = event.get("event", "")
        status: str = event.get("status", "")

        is_positive_pattern = _event_matches(event_name, defn["positive_patterns"])
        is_negative_pattern = _event_matches(event_name, defn["negative_patterns"])

        if not (is_positive_pattern or is_negative_pattern):
            continue  # irrelevant event

        if status in defn["positive_statuses"]:
            positives += 1
        elif status in defn["negative_statuses"]:
            negatives += 1
        elif is_negative_pattern:
            # A negative-pattern event with an unknown status counts as negative
            negatives += 1
        else:
            # A positive-pattern event with an unknown status counts as neutral
            positives += 1

    score = (positives + 1) / (positives + negatives + 2)
    return round(score, 4)


def compute_compliance_scores(events: List[Dict]) -> Dict[str, float]:
    """Return a compliance score for each regulation given a list of audit events.

    Example output::

        {"PDPA": 0.9, "GDPR": 0.85, "EU_AI_Act": 0.8}
    """
    return {regulation: _score_for_regulation(events, regulation) for regulation in REGULATION_DEFINITIONS}
