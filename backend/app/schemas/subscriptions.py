"""Pydantic schemas for subscription request/response payloads."""

from pydantic import BaseModel, Field


class SubscriptionCreateRequest(BaseModel):
    """Input payload for creating or refreshing a subscriber."""

    phone_e164: str = Field(..., min_length=8, max_length=20)
    display_name: str | None = Field(default=None, max_length=120)


class UnsubscribeRequest(BaseModel):
    """Input payload for unsubscribing a phone number."""

    phone_e164: str = Field(..., min_length=8, max_length=20)


class SubscriptionResponse(BaseModel):
    """Response payload returned by subscription endpoints."""

    id: str
    phone_e164: str
    whatsapp_status: str
