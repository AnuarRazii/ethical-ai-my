from dataclasses import dataclass
import os
from pathlib import Path


@dataclass(frozen=True)
class Settings:
    audit_log_path: Path
    api_key: str


def get_settings() -> Settings:
    repo_root = Path(__file__).resolve().parents[2]
    return Settings(
        audit_log_path=Path(
            os.getenv("AUDIT_LOG_PATH", repo_root / "data" / "audit_logs.jsonl")
        ),
        api_key=os.getenv("AUDIT_API_KEY", "dev-local-key"),
    )
