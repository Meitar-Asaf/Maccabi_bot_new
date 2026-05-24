from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.subscriptions import (
    SubscriptionCreateRequest,
    SubscriptionResponse,
    UnsubscribeRequest,
)
from app.services.subscriptions import unsubscribe, upsert_subscription

router = APIRouter(prefix="/subscriptions")


@router.post("", response_model=SubscriptionResponse)
def create_subscription(payload: SubscriptionCreateRequest, db: Session = Depends(get_db)) -> SubscriptionResponse:
    user = upsert_subscription(db, payload.phone_e164, payload.display_name)
    return SubscriptionResponse(id=user.id, phone_e164=user.phone_e164, whatsapp_status=user.whatsapp_status)


@router.post("/unsubscribe", response_model=SubscriptionResponse)
def create_unsubscribe(payload: UnsubscribeRequest, db: Session = Depends(get_db)) -> SubscriptionResponse:
    user = unsubscribe(db, payload.phone_e164)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Subscriber not found")
    return SubscriptionResponse(id=user.id, phone_e164=user.phone_e164, whatsapp_status=user.whatsapp_status)
