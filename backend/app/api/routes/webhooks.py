"""Inbound webhook endpoints for external messaging providers."""

from datetime import datetime

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.user import User

router = APIRouter(prefix="/webhooks")


class WhatsAppInboundPayload(BaseModel):
    """Inbound WhatsApp message payload used for keyword-based opt flow."""

    phone_e164: str
    message_text: str


@router.post("/whatsapp/inbound")
def whatsapp_inbound(payload: WhatsAppInboundPayload, db: Session = Depends(get_db)) -> dict[str, str]:
    """Handle inbound WhatsApp keywords and update subscription status."""

    normalized = payload.message_text.strip().lower()
    user = db.execute(select(User).where(User.phone_e164 == payload.phone_e164)).scalar_one_or_none()

    if user is None:
        user = User(
            phone_e164=payload.phone_e164,
            whatsapp_status="pending_opt_in",
            consent_source="whatsapp_inbound",
        )
        db.add(user)

    user.last_inbound_at = datetime.utcnow()

    if normalized in {"start", "subscribe", "join"}:
        user.whatsapp_status = "active"
        user.consented_at = datetime.utcnow()
    elif normalized in {"stop", "unsubscribe", "leave"}:
        user.whatsapp_status = "unsubscribed"
        user.unsubscribed_at = datetime.utcnow()

    db.commit()
    return {"status": "ok"}
