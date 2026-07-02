#!/usr/bin/env python3
"""Generate audit evidence exports from RZ1 audit and risk logs."""

from __future__ import annotations

import argparse
import datetime as dt
import json
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Sequence, Tuple

DEFAULT_LOG_SOURCES = (
    Path("/tmp/rz1_audit_events.jsonl"),
    Path("/tmp/rz1_audit_log.json"),
    Path("/tmp/rz1_risk_score.json"),
)
DEFAULT_JSON_OUTPUT = Path("audit_report.json")
DEFAULT_MARKDOWN_OUTPUT = Path("audit_report.md")
GOVERNANCE_VERSION_FILE = Path("governance/version.json")


def utc_now() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat().replace("+00:00", "Z")


def load_version_metadata() -> Dict[str, str]:
    defaults = {
        "output_version": "RZ1-1.0",
        "governance_version": "1.0",
        "traceability_standard": "RZ1-TRACE",
    }
    if not GOVERNANCE_VERSION_FILE.exists():
        return defaults

    payload = json.loads(GOVERNANCE_VERSION_FILE.read_text(encoding="utf-8"))
    return {
        "output_version": str(payload.get("output_version", defaults["output_version"])),
        "governance_version": str(payload.get("governance_version", defaults["governance_version"])),
        "traceability_standard": str(
            payload.get("traceability_standard", defaults["traceability_standard"])
        ),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate audit evidence exports from RZ1 logs.")
    parser.add_argument(
        "logs",
        nargs="*",
        help="Optional log files or directories. Defaults to common RZ1 log paths in /tmp.",
    )
    parser.add_argument("--output-json", default=str(DEFAULT_JSON_OUTPUT), help="JSON report output path")
    parser.add_argument(
        "--output-markdown",
        default=str(DEFAULT_MARKDOWN_OUTPUT),
        help="Markdown report output path",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit with a non-zero code if any compliance check fails.",
    )
    return parser.parse_args()


def existing_sources(raw_sources: Sequence[str]) -> List[Path]:
    candidates = [Path(item) for item in raw_sources] if raw_sources else list(DEFAULT_LOG_SOURCES)
    existing: List[Path] = []
    seen: set[Path] = set()
    for candidate in candidates:
        resolved = candidate.resolve(strict=False)
        if resolved in seen or not candidate.exists():
            continue
        seen.add(resolved)
        existing.append(candidate)
    return existing


def iter_source_files(source: Path) -> Iterable[Path]:
    if source.is_dir():
        for suffix in ("*.json", "*.jsonl"):
            for file_path in sorted(source.rglob(suffix)):
                if file_path.is_file():
                    yield file_path
        return
    yield source


def timestamp_for(record: Dict[str, Any]) -> str:
    return str(record.get("created_at") or record.get("generated_at") or "")


def flatten_payload(payload: Any) -> List[Dict[str, Any]]:
    if isinstance(payload, dict):
        if payload.get("record_type") in {"audit_event", "risk_assessment"}:
            return [payload]
        flattened: List[Dict[str, Any]] = []
        for key in ("events", "records", "items"):
            value = payload.get(key)
            if isinstance(value, list):
                for item in value:
                    flattened.extend(flatten_payload(item))
        for key in ("event", "risk", "data"):
            value = payload.get(key)
            if isinstance(value, (dict, list)):
                flattened.extend(flatten_payload(value))
        return flattened
    if isinstance(payload, list):
        flattened = []
        for item in payload:
            flattened.extend(flatten_payload(item))
        return flattened
    return []


def load_records_from_file(file_path: Path) -> List[Dict[str, Any]]:
    if file_path.suffix == ".jsonl":
        records: List[Dict[str, Any]] = []
        for line in file_path.read_text(encoding="utf-8").splitlines():
            raw = line.strip()
            if not raw:
                continue
            records.extend(flatten_payload(json.loads(raw)))
        return records
    return flatten_payload(json.loads(file_path.read_text(encoding="utf-8")))


def load_records(sources: Sequence[Path]) -> Tuple[List[Dict[str, Any]], List[str]]:
    records: List[Dict[str, Any]] = []
    used_sources: List[str] = []
    for source in sources:
        source_files = list(iter_source_files(source))
        if not source_files:
            continue
        for file_path in source_files:
            loaded = load_records_from_file(file_path)
            if not loaded:
                continue
            records.extend(loaded)
            used_sources.append(str(file_path))
    return records, used_sources


def check(name: str, passed: bool, detail: str) -> Dict[str, str]:
    return {
        "name": name,
        "status": "pass" if passed else "fail",
        "detail": detail,
    }


def summarize_trace(trace_id: str, records: Sequence[Dict[str, Any]]) -> Dict[str, Any]:
    ordered = sorted(records, key=timestamp_for)
    events = [record for record in ordered if record.get("record_type") == "audit_event"]
    risks = [record for record in ordered if record.get("record_type") == "risk_assessment"]
    timestamps = [timestamp for timestamp in (timestamp_for(record) for record in ordered) if timestamp]
    risk_scores = [int(record["risk_score"]) for record in risks if "risk_score" in record]

    return {
        "trace_id": trace_id,
        "timestamps": timestamps,
        "risk_scores": risk_scores,
        "latest_risk_score": risk_scores[-1] if risk_scores else None,
        "latest_risk_level": risks[-1].get("risk_level") if risks else None,
        "events": [
            {
                "timestamp": timestamp_for(event),
                "event": event.get("event"),
                "actor": event.get("actor"),
                "status": event.get("status"),
                "source": event.get("source"),
                "details": event.get("details", {}),
            }
            for event in events
        ],
        "compliance_checks": [
            check("timestamps_present", len(timestamps) == len(ordered), f"{len(timestamps)}/{len(ordered)} records contain timestamps"),
            check("has_audit_event", bool(events), f"{len(events)} audit event record(s) linked to trace"),
            check("has_risk_assessment", bool(risks), f"{len(risks)} risk assessment record(s) linked to trace"),
        ],
    }


def build_report(records: Sequence[Dict[str, Any]], used_sources: Sequence[str]) -> Dict[str, Any]:
    metadata = load_version_metadata()
    grouped: dict[str, List[Dict[str, Any]]] = defaultdict(list)
    missing_trace_id = 0
    timestamped_records = 0
    risk_scores_valid = 0
    risk_scores_total = 0

    for record in records:
        trace_id = str(record.get("trace_id") or "").strip()
        if trace_id:
            grouped[trace_id].append(record)
        else:
            missing_trace_id += 1

        if timestamp_for(record):
            timestamped_records += 1

        if record.get("record_type") == "risk_assessment":
            risk_scores_total += 1
            score = record.get("risk_score")
            if isinstance(score, int) and 1 <= score <= 100:
                risk_scores_valid += 1

    traces = [summarize_trace(trace_id, grouped[trace_id]) for trace_id in sorted(grouped)]
    audit_event_count = sum(1 for record in records if record.get("record_type") == "audit_event")
    risk_assessment_count = sum(1 for record in records if record.get("record_type") == "risk_assessment")

    trace_check_failures = sum(
        1 for trace in traces if any(item["status"] != "pass" for item in trace["compliance_checks"])
    )

    compliance_checks = [
        check("records_found", bool(records), f"{len(records)} record(s) parsed from {len(used_sources)} source file(s)"),
        check(
            "trace_ids_present",
            missing_trace_id == 0,
            f"{len(records) - missing_trace_id}/{len(records)} record(s) contain trace_id" if records else "0/0 record(s) contain trace_id",
        ),
        check(
            "timestamps_present",
            timestamped_records == len(records),
            f"{timestamped_records}/{len(records)} record(s) contain timestamps" if records else "0/0 record(s) contain timestamps",
        ),
        check(
            "risk_scores_valid",
            risk_scores_total == risk_scores_valid,
            f"{risk_scores_valid}/{risk_scores_total} risk assessment record(s) have scores in range 1-100"
            if risk_scores_total
            else "0/0 risk assessment record(s) have scores in range 1-100",
        ),
        check(
            "compliance_coverage",
            trace_check_failures == 0,
            f"{len(traces) - trace_check_failures}/{len(traces)} trace group(s) passed all compliance checks"
            if traces
            else "0/0 trace group(s) passed all compliance checks",
        ),
    ]

    return {
        "output_version": metadata["output_version"],
        "governance_version": metadata["governance_version"],
        "traceability_standard": metadata["traceability_standard"],
        "report_type": "audit_evidence_export",
        "generated_at": utc_now(),
        "sources": list(used_sources),
        "summary": {
            "total_records": len(records),
            "total_traces": len(traces),
            "audit_event_count": audit_event_count,
            "risk_assessment_count": risk_assessment_count,
        },
        "compliance_checks": compliance_checks,
        "traces": traces,
    }


def render_markdown(report: Dict[str, Any]) -> str:
    lines = [
        "# Audit Evidence Report",
        "",
        f"- Generated at: {report['generated_at']}",
        f"- Output version: {report['output_version']}",
        f"- Governance version: {report['governance_version']}",
        f"- Traceability standard: {report['traceability_standard']}",
        "",
        "## Summary",
        "",
        f"- Source files: {len(report['sources'])}",
        f"- Total records: {report['summary']['total_records']}",
        f"- Total traces: {report['summary']['total_traces']}",
        f"- Audit events: {report['summary']['audit_event_count']}",
        f"- Risk assessments: {report['summary']['risk_assessment_count']}",
        "",
        "## Compliance Checks",
        "",
    ]

    for item in report["compliance_checks"]:
        marker = "PASS" if item["status"] == "pass" else "FAIL"
        lines.append(f"- [{marker}] {item['name']}: {item['detail']}")

    lines.extend(["", "## Sources", ""])
    if report["sources"]:
        lines.extend(f"- `{source}`" for source in report["sources"])
    else:
        lines.append("- No matching log files were found.")

    lines.extend(["", "## Trace Records", ""])
    if not report["traces"]:
        lines.append("No trace records were available.")
        return "\n".join(lines) + "\n"

    for trace in report["traces"]:
        lines.extend(
            [
                f"### Trace {trace['trace_id']}",
                "",
                f"- Timestamps: {', '.join(trace['timestamps']) if trace['timestamps'] else 'None'}",
                f"- Latest risk score: {trace['latest_risk_score'] if trace['latest_risk_score'] is not None else 'None'}",
                f"- Latest risk level: {trace['latest_risk_level'] or 'None'}",
                "",
                "#### Compliance Checks",
                "",
            ]
        )
        for item in trace["compliance_checks"]:
            marker = "PASS" if item["status"] == "pass" else "FAIL"
            lines.append(f"- [{marker}] {item['name']}: {item['detail']}")

        lines.extend(["", "#### Audit Events", ""])
        if trace["events"]:
            for event in trace["events"]:
                lines.append(
                    f"- {event['timestamp']}: `{event['event']}` by `{event['actor']}` "
                    f"status=`{event['status']}` source=`{event['source']}`"
                )
        else:
            lines.append("- No audit events linked to this trace.")

        lines.append("")

    return "\n".join(lines) + "\n"


def write_output(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def main() -> int:
    args = parse_args()
    sources = existing_sources(args.logs)
    records, used_sources = load_records(sources)
    report = build_report(records, used_sources)

    json_output = Path(args.output_json)
    markdown_output = Path(args.output_markdown)

    write_output(json_output, json.dumps(report, indent=2) + "\n")
    write_output(markdown_output, render_markdown(report))

    strict_failed = any(item["status"] != "pass" for item in report["compliance_checks"])
    print(f"Wrote {json_output}")
    print(f"Wrote {markdown_output}")
    return 1 if args.strict and strict_failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
