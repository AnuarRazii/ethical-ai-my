from fastapi import FastAPI

from app.api.routes import audit, consent
from app.middleware.audit_middleware import AuditMiddleware


app = FastAPI(title="Ethical AI MY Audit Service", version="0.1.0")
app.add_middleware(AuditMiddleware)
app.include_router(consent.router, prefix="/consent", tags=["consent"])
app.include_router(audit.router, prefix="/audit", tags=["audit"])


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
