import json
from datetime import datetime, timedelta

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.integrations.highlight_resolver import HighlightResolver
from app.integrations.sports_client import SportsClient
from app.integrations.whatsapp_client import WhatsAppClient
from app.models.match_tracking import MatchEvent, MessageDelivery, NotificationJob
from app.models.user import User


def _compose_message(event: MatchEvent, stats: dict, highlight_url: str | None) -> str:
    scoreline = stats.get("scoreline", "Live score unavailable")
    return (
        f"GOAL! {event.scorer_name or 'Unknown scorer'} ({event.minute or '?'}')\n"
        f"Score: {scoreline}\n"
        f"Tackles: {stats.get('successful_tackles', 'n/a')} | Passes: {stats.get('successful_passes', 'n/a')}\n"
        f"Highlight: {highlight_url or 'Not found yet'}"
    )


def process_due_jobs(
    db: Session,
    resolver: HighlightResolver,
    sports_client: SportsClient,
    whatsapp_client: WhatsAppClient,
) -> dict[str, int]:
    now = datetime.utcnow()
    jobs = list(
        db.execute(
            select(NotificationJob).where(
                NotificationJob.status.in_(["queued", "retry"]),
                NotificationJob.run_after <= now,
            )
        ).scalars().all()
    )

    sent = 0
    retried = 0
    failed = 0

    for job in jobs:
        job.status = "processing"
        job.attempt_count += 1

        event = db.execute(select(MatchEvent).where(MatchEvent.id == job.match_event_id)).scalar_one_or_none()
        if event is None:
            job.status = "failed"
            job.last_error = "Missing match event"
            failed += 1
            continue

        payload = json.loads(job.payload_json or "{}")
        match_external_id = payload.get("match_external_id", "")
        scorer_name = payload.get("scorer_name", event.scorer_name or "")
        minute = payload.get("minute", event.minute or 0)

        highlight_url = resolver.find_highlight_url(match_external_id, scorer_name, minute)
        if highlight_url is None and job.attempt_count < job.max_attempts:
            job.status = "retry"
            job.run_after = datetime.utcnow() + timedelta(minutes=2)
            retried += 1
            continue

        subscribers = list(
            db.execute(select(User).where(User.whatsapp_status == "active")).scalars().all()
        )
        stats = sports_client.fetch_match_stats(match_external_id)
        message_text = _compose_message(event, stats, highlight_url)

        for user in subscribers:
            result = whatsapp_client.send_goal_update(
                to_phone=user.phone_e164,
                text=message_text,
                highlight_url=highlight_url,
            )
            delivery = MessageDelivery(
                notification_job_id=job.id,
                user_id=user.id,
                provider_message_id=result.provider_message_id,
                status="sent" if result.ok else "failed",
                error_text=result.error,
                sent_at=datetime.utcnow() if result.ok else None,
            )
            db.add(delivery)

        job.status = "sent" if highlight_url is not None else "completed_without_highlight"
        sent += 1

    db.commit()
    return {"sent": sent, "retried": retried, "failed": failed}
