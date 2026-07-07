from __future__ import annotations

import json
from pathlib import Path

from app.audit.hash_chain import GENESIS_HASH, compute_chain_hash
from app.audit.models import AuditEvent


class AuditLogger:
    def __init__(self, log_path: Path) -> None:
        self.log_path = log_path
        self.log_path.parent.mkdir(parents=True, exist_ok=True)
        if not self.log_path.exists():
            self.log_path.touch()

    def _last_hash(self) -> str:
        last_line = ""
        with self.log_path.open("r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    last_line = line
        if not last_line:
            return GENESIS_HASH
        parsed = json.loads(last_line)
        return parsed.get("chain_hash", GENESIS_HASH)

    def write(self, event: AuditEvent) -> dict:
        payload = event.model_dump(mode="json")
        previous_hash = self._last_hash()
        chain_hash = compute_chain_hash(payload, previous_hash)
        wrapped = {
            "previous_hash": previous_hash,
            "chain_hash": chain_hash,
            "event": payload,
        }
        with self.log_path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(wrapped, ensure_ascii=False) + "\n")
        return wrapped

    def tail(self, limit: int = 50) -> list[dict]:
        lines = self.log_path.read_text(encoding="utf-8").splitlines()
        return [json.loads(line) for line in lines[-max(0, limit) :] if line.strip()]
