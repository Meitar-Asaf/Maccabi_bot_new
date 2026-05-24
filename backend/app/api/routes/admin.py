from fastapi import APIRouter, Depends
from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.integrations.highlight_resolver import HighlightResolver
from app.integrations.sports_client import SportsClient
from app.integrations.whatsapp_client import WhatsAppClient
from app.models.match_tracking import Match, NotificationJob
from app.models.user import User
from app.schemas.admin import JobsHealthResponse, SubscriberSummaryResponse
from app.services.live_matches import poll_live_matches
from app.services.notifications import process_due_jobs

router = APIRouter(prefix="/admin")


@router.get("/subscribers/summary", response_model=SubscriberSummaryResponse)
def subscriber_summary(db: Session = Depends(get_db)) -> SubscriberSummaryResponse:
    active = db.execute(select(func.count()).select_from(User).where(User.whatsapp_status == "active")).scalar_one()
    pending = db.execute(
        select(func.count()).select_from(User).where(User.whatsapp_status == "pending_opt_in")
    ).scalar_one()
    unsubscribed = db.execute(
        select(func.count()).select_from(User).where(User.whatsapp_status == "unsubscribed")
    ).scalar_one()
    return SubscriberSummaryResponse(active=active, pending_opt_in=pending, unsubscribed=unsubscribed)


@router.get("/notifications/jobs", response_model=JobsHealthResponse)
def notifications_jobs_health(db: Session = Depends(get_db)) -> JobsHealthResponse:
    queued = db.execute(select(func.count()).select_from(NotificationJob).where(NotificationJob.status == "queued")).scalar_one()
    processing = db.execute(
        select(func.count()).select_from(NotificationJob).where(NotificationJob.status == "processing")
    ).scalar_one()
    failed = db.execute(select(func.count()).select_from(NotificationJob).where(NotificationJob.status == "failed")).scalar_one()
    sent = db.execute(
        select(func.count()).select_from(NotificationJob).where(NotificationJob.status.in_(["sent", "completed_without_highlight"]))
    ).scalar_one()
    return JobsHealthResponse(queued=queued, processing=processing, failed=failed, sent=sent)


@router.post("/poll-live")
def trigger_poll_live(db: Session = Depends(get_db)) -> dict[str, int]:
    created_jobs = poll_live_matches(db, SportsClient())
    return {"created_jobs": created_jobs}


@router.post("/process-notifications")
def trigger_process_notifications(db: Session = Depends(get_db)) -> dict[str, int]:
    return process_due_jobs(db, HighlightResolver(), SportsClient(), WhatsAppClient())


@router.get("/matches/live")
def get_live_matches(db: Session = Depends(get_db)) -> list[dict]:
    live = list(db.execute(select(Match).where(Match.status.in_(["live", "in_progress"]))).scalars().all())
    return [
        {
            "id": m.id,
            "external_match_id": m.external_match_id,
            "home_team": m.home_team,
            "away_team": m.away_team,
            "home_score": m.home_score,
            "away_score": m.away_score,
            "status": m.status,
        }
        for m in live
    ]
