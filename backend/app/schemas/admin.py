from pydantic import BaseModel


class SubscriberSummaryResponse(BaseModel):
    active: int
    pending_opt_in: int
    unsubscribed: int


class JobsHealthResponse(BaseModel):
    queued: int
    processing: int
    failed: int
    sent: int
