from app.consent.models import ConsentRecord


class ConsentRegistry:
    def __init__(self) -> None:
        self._records: dict[str, ConsentRecord] = {}

    def upsert(self, record: ConsentRecord) -> ConsentRecord:
        self._records[record.consent_id] = record
        return record

    def is_valid(self, consent_id: str | None) -> bool:
        if not consent_id:
            return False
        record = self._records.get(consent_id)
        return bool(record and record.granted)

    def get(self, consent_id: str) -> ConsentRecord | None:
        return self._records.get(consent_id)


registry = ConsentRegistry()
