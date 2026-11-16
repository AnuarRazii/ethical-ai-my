from datetime import datetime, timezone
from pydantic import BaseModel, Field


class ConsentRecord(BaseModel):
    consent_id: str
    subject_id: str
    purpose: str
    granted: bool = True
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
