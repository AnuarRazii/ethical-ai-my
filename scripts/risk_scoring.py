#!/usr/bin/env python3
"""RZ1 risk scoring with versioned and traceable JSON output."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import uuid
from typing import Dict


def utc_now() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat().replace("+00:00", "Z")


def risk_level(score: int) -> str:
    if score <= 20:
        return "low"
    if score <= 40:
        return "moderate"
    if score <= 60:
        return "high"
    if score <= 80:
        return "very_high"
    return "critical"


def bounded_factor(value: int) -> int:
    return max(1, min(5, value))


def build_result(args: argparse.Namespace) -> Dict[str, object]:
    impact = bounded_factor(args.impact)
    likelihood = bounded_factor(args.likelihood)
    detectability = bounded_factor(args.detectability)
    control_strength = bounded_factor(args.control_strength)

    raw_score = (impact * likelihood) + detectability - control_strength
    risk_score = max(1, min(100, raw_score * 5))

    return {
        "output_version": args.output_version,
        "governance_version": args.governance_version,
        "record_type": "risk_assessment",
        "generated_at": utc_now(),
        "trace_id": args.trace_id or str(uuid.uuid4()),
        "context": args.context,
        "inputs": {
            "impact": impact,
            "likelihood": likelihood,
            "detectability": detectability,
            "control_strength": control_strength,
        },
        "risk_score": risk_score,
        "risk_level": risk_level(risk_score),
        "source": "scripts/risk_scoring.py",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate RZ1 JSON risk scoring records.")
    parser.add_argument("--impact", type=int, required=True)
    parser.add_argument("--likelihood", type=int, required=True)
    parser.add_argument("--detectability", type=int, required=True)
    parser.add_argument("--control-strength", dest="control_strength", type=int, required=True)
    parser.add_argument("--context", default="governance")
    parser.add_argument("--trace-id", dest="trace_id", default="")
    parser.add_argument("--output-version", default="RZ1-1.0")
    parser.add_argument("--governance-version", default="1.0")
    parser.add_argument("--output", default="")
    args = parser.parse_args()

    result = build_result(args)
    payload = json.dumps(result, indent=2)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as handle:
            handle.write(payload + "\n")
    print(payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
