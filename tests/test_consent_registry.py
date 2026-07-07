from app.consent.models import ConsentRecord
from app.consent.registry import ConsentRegistry


def test_registry_validates_granted_consent() -> None:
    registry = ConsentRegistry()
    record = ConsentRecord(consent_id="c-1", subject_id="u-1", purpose="analytics")
    registry.upsert(record)
    assert registry.is_valid("c-1") is True
