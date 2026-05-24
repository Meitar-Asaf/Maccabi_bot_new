from pydantic import BaseModel, Field


class SubscriptionCreateRequest(BaseModel):
    phone_e164: str = Field(..., min_length=8, max_length=20)
    display_name: str | None = Field(default=None, max_length=120)


class UnsubscribeRequest(BaseModel):
    phone_e164: str = Field(..., min_length=8, max_length=20)


class SubscriptionResponse(BaseModel):
    id: str
    phone_e164: str
    whatsapp_status: str
