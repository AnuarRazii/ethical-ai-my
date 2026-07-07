from fastapi import APIRouter, HTTPException

from app.consent.models import ConsentRecord
from app.consent.registry import registry


router = APIRouter()


@router.post("/", response_model=ConsentRecord)
def grant_consent(payload: ConsentRecord) -> ConsentRecord:
    return registry.upsert(payload)


@router.get("/{consent_id}", response_model=ConsentRecord)
def get_consent(consent_id: str) -> ConsentRecord:
    record = registry.get(consent_id)
    if not record:
        raise HTTPException(status_code=404, detail="Consent record not found")
    return record
