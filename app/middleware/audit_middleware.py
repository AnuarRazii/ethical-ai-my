from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

from app.audit.logger import AuditLogger
from app.audit.models import AuditEvent
from app.consent.registry import registry
from app.core.config import get_settings
from app.core.security import pseudonymize_identifier


class AuditMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next) -> Response:
        response = await call_next(request)

        consent_id = request.headers.get("X-Consent-Id")
        subject = request.headers.get("X-Subject-Id", "anonymous")
        is_consent_valid = registry.is_valid(consent_id)
        logger = AuditLogger(get_settings().audit_log_path)
        event = AuditEvent(
            actor=pseudonymize_identifier(subject),
            action=f"{request.method} {request.url.path}",
            origin="user_input",
            consent_id=consent_id,
            processing_trace=["http_request", "route_handler", "http_response"],
            retention_policy="30_days_default",
            access_log=["audit_middleware", "api_router"],
            metadata={
                "status_code": response.status_code,
                "consent_valid": is_consent_valid,
                "client": request.client.host if request.client else "unknown",
            },
        )
        logger.write(event)
        return response
