from fastapi import APIRouter, Query

from app.audit.logger import AuditLogger
from app.core.config import get_settings


router = APIRouter()
audit_logger = AuditLogger(get_settings().audit_log_path)


@router.get("/logs")
def get_audit_logs(limit: int = Query(default=50, ge=1, le=500)) -> dict:
    return {"items": audit_logger.tail(limit=limit)}
