"""Pydantic schemas for admin monitoring endpoints."""

from pydantic import BaseModel


class SubscriberSummaryResponse(BaseModel):
    """Aggregated subscriber counters by status."""

    active: int
    pending_opt_in: int
    unsubscribed: int


class JobsHealthResponse(BaseModel):
    """Aggregated notification job counters by processing state."""

    queued: int
    processing: int
    failed: int
    sent: int
