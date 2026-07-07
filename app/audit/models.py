from datetime import datetime, timezone
from pydantic import BaseModel, Field


class AuditEvent(BaseModel):
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    actor: str
    action: str
    origin: str
    consent_id: str | None = None
    processing_trace: list[str] = Field(default_factory=list)
    retention_policy: str = "default"
    access_log: list[str] = Field(default_factory=list)
    metadata: dict = Field(default_factory=dict)
