"""FastAPI application entrypoint and middleware wiring."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.router import api_router
from app.core.config import settings

app = FastAPI(title=settings.app_name)

allowed_origins = [origin.strip() for origin in settings.cors_allowed_origins.split(",") if origin.strip()]
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins if allowed_origins else ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=settings.api_prefix)


@app.get("/health")
def health() -> dict[str, str]:
    """Return a lightweight liveness response for health checks."""
    return {"status": "ok"}


@app.get("/")
def root() -> dict[str, str]:
    """Return basic service metadata for quick diagnostics."""
    return {"service": settings.app_name, "health": "/health"}
