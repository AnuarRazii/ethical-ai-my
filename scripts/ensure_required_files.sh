#!/usr/bin/env bash
set -euo pipefail

ensure_dir() {
  local dir="$1"
  if [ ! -d "$dir" ]; then
    mkdir -p "$dir"
    echo "⚠️ Auto-created missing directory: $dir"
  fi
}

ensure_file() {
  local file="$1"
  local content="$2"
  if [ ! -f "$file" ]; then
    printf "%s\n" "$content" > "$file"
    echo "⚠️ Auto-created missing file: $file"
  fi
}

ensure_file "README.md" "# Ethical AI MY

**Open, Auditable, Non-Mandatory Reference**
"
ensure_file "LICENSE" "Creative Commons Attribution 4.0 International (CC BY 4.0)"
ensure_file "ETHICS.md" "# ETHICS.md

## Core Ethical Principles

Version 1.0 | Release Date: 2026-06-01
"
ensure_file "GOVERNANCE.md" "# GOVERNANCE.md

Version 1.0 | Release Date: 2026-06-01
"
ensure_file "SECURITY.md" "# SECURITY.md

Security standards for Ethical AI MY.
"
ensure_file "CODE_OF_CONDUCT.md" "# CODE_OF_CONDUCT.md

Community participation standards.
"
ensure_file "ATTRIBUTION.md" "# ATTRIBUTION.md

Contributor recognition and citations.
"
ensure_file "FINAL_INTENT.md" "# FINAL_INTENT.md

Reference intent statement.
"
ensure_file "RELEASE_NOTES.md" "# RELEASE_NOTES.md

- **Version:** 1.0
- **Release Date:** 2026-06-01
"
ensure_dir "governance"
ensure_file "governance/version.json" "{
  \"output_version\": \"RZ1-1.0\",
  \"governance_version\": \"1.0\",
  \"release_date\": \"2026-06-01\"
}"

ensure_dir "scripts"
if [ ! -f "scripts/audit_logger.py" ]; then
  cat > "scripts/audit_logger.py" <<'PY'
#!/usr/bin/env python3
import argparse, datetime, json, uuid

p = argparse.ArgumentParser()
p.add_argument("--event", required=True)
p.add_argument("--actor", default="system")
p.add_argument("--status", default="ok")
p.add_argument("--output")
args = p.parse_args()

record = {
    "output_version": "RZ1-1.0",
    "governance_version": "1.0",
    "record_type": "audit_event",
    "event_id": str(uuid.uuid4()),
    "trace_id": str(uuid.uuid4()),
    "created_at": datetime.datetime.now(datetime.timezone.utc).isoformat().replace("+00:00", "Z"),
    "event": args.event,
    "actor": args.actor,
    "status": args.status,
}
payload = json.dumps(record, indent=2)
if args.output:
    open(args.output, "w", encoding="utf-8").write(payload + "\n")
print(payload)
PY
  chmod +x "scripts/audit_logger.py"
  echo "⚠️ Auto-created missing file: scripts/audit_logger.py"
fi

if [ ! -f "scripts/risk_scoring.py" ]; then
  cat > "scripts/risk_scoring.py" <<'PY'
#!/usr/bin/env python3
import argparse, datetime, json, uuid

def level(score):
    return "low" if score <= 20 else "moderate" if score <= 40 else "high" if score <= 60 else "very_high" if score <= 80 else "critical"

p = argparse.ArgumentParser()
p.add_argument("--impact", type=int, required=True)
p.add_argument("--likelihood", type=int, required=True)
p.add_argument("--detectability", type=int, required=True)
p.add_argument("--control-strength", type=int, required=True)
p.add_argument("--output")
args = p.parse_args()

raw = (args.impact * args.likelihood) + args.detectability - args.control_strength
score = max(1, min(100, raw * 5))
record = {
    "output_version": "RZ1-1.0",
    "governance_version": "1.0",
    "record_type": "risk_assessment",
    "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat().replace("+00:00", "Z"),
    "trace_id": str(uuid.uuid4()),
    "risk_score": score,
    "risk_level": level(score),
}
payload = json.dumps(record, indent=2)
if args.output:
    open(args.output, "w", encoding="utf-8").write(payload + "\n")
print(payload)
PY
  chmod +x "scripts/risk_scoring.py"
  echo "⚠️ Auto-created missing file: scripts/risk_scoring.py"
fi

ensure_dir "api"
if [ ! -f "api/audit_api.py" ]; then
  cat > "api/audit_api.py" <<'PY'
#!/usr/bin/env python3
import argparse, datetime, json, uuid
from http.server import BaseHTTPRequestHandler, HTTPServer

def payload(data):
    return {
        "output_version": "RZ1-1.0",
        "governance_version": "1.0",
        "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat().replace("+00:00", "Z"),
        "trace_id": str(uuid.uuid4()),
        "data": data,
    }

class H(BaseHTTPRequestHandler):
    def _send(self, code, obj):
        raw = json.dumps(obj).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(raw)))
        self.end_headers()
        self.wfile.write(raw)
    def do_GET(self):
        if self.path == "/health":
            self._send(200, payload({"status": "ok"})); return
        if self.path == "/version":
            self._send(200, payload({"api_version": "RZ1-1.0"})); return
        self._send(404, payload({"error": "not_found"}))
    def do_POST(self):
        if self.path == "/audit/events":
            self._send(201, payload({"accepted": True})); return
        self._send(404, payload({"error": "not_found"}))

if __name__ == "__main__":
    a = argparse.ArgumentParser()
    a.add_argument("--host", default="127.0.0.1")
    a.add_argument("--port", type=int, default=8080)
    args = a.parse_args()
    HTTPServer((args.host, args.port), H).serve_forever()
PY
  chmod +x "api/audit_api.py"
  echo "⚠️ Auto-created missing file: api/audit_api.py"
fi

echo "✅ Required files check completed"
