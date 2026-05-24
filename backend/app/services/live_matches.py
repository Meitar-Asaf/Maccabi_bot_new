import json
from datetime import datetime, timedelta

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.config import settings
from app.integrations.sports_client import SportsClient
from app.models.match_tracking import Match, MatchEvent, NotificationJob


def poll_live_matches(db: Session, sports_client: SportsClient) -> int:
    events = sports_client.fetch_live_goals()
    created_jobs = 0

    for event in events:
        existing_event = db.execute(
            select(MatchEvent).where(MatchEvent.external_event_id == event.external_event_id)
        ).scalar_one_or_none()
        if existing_event is not None:
            continue

        match = db.execute(select(Match).where(Match.external_match_id == event.match_external_id)).scalar_one_or_none()
        if match is None:
            match = Match(
                external_match_id=event.match_external_id,
                home_team="Unknown",
                away_team="Unknown",
                status="live",
                kickoff_at=event.event_time,
                last_polled_at=datetime.utcnow(),
            )
            db.add(match)
            db.flush()

        match_event = MatchEvent(
            external_event_id=event.external_event_id,
            match_id=match.id,
            event_type="goal",
            team_name=event.team_name,
            scorer_name=event.scorer_name,
            minute=event.minute,
            payload_json=json.dumps({"source": "sports_client"}),
            event_time=event.event_time,
        )
        db.add(match_event)
        db.flush()

        job = NotificationJob(
            match_event_id=match_event.id,
            job_type="goal_highlight",
            status="queued",
            run_after=datetime.utcnow() + timedelta(seconds=settings.highlight_search_delay_seconds),
            payload_json=json.dumps(
                {
                    "match_external_id": event.match_external_id,
                    "scorer_name": event.scorer_name,
                    "minute": event.minute,
                }
            ),
        )
        db.add(job)
        created_jobs += 1

    db.commit()
    return created_jobs
