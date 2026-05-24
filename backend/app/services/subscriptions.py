from datetime import datetime

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.user import User


def upsert_subscription(db: Session, phone_e164: str, display_name: str | None) -> User:
    stmt = select(User).where(User.phone_e164 == phone_e164)
    user = db.execute(stmt).scalar_one_or_none()

    if user is None:
        user = User(
            phone_e164=phone_e164,
            display_name=display_name,
            whatsapp_status="pending_opt_in",
            consent_source="landing_page",
        )
        db.add(user)
    else:
        user.display_name = display_name or user.display_name
        if user.whatsapp_status == "unsubscribed":
            user.whatsapp_status = "pending_opt_in"
            user.unsubscribed_at = None

    db.commit()
    db.refresh(user)
    return user


def unsubscribe(db: Session, phone_e164: str) -> User | None:
    stmt = select(User).where(User.phone_e164 == phone_e164)
    user = db.execute(stmt).scalar_one_or_none()
    if user is None:
        return None

    user.whatsapp_status = "unsubscribed"
    user.unsubscribed_at = datetime.utcnow()
    db.commit()
    db.refresh(user)
    return user
