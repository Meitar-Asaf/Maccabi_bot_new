"""Sports provider integration adapter interfaces and payload types."""

from dataclasses import dataclass
from datetime import datetime


@dataclass
class GoalEventPayload:
    """Normalized goal event payload returned by sports feed adapters."""

    external_event_id: str
    match_external_id: str
    scorer_name: str
    minute: int
    team_name: str
    event_time: datetime


class SportsClient:
    """Stub sports client used by the scaffold until real provider wiring is added."""

    def fetch_live_goals(self) -> list[GoalEventPayload]:
        """Return live goal events in normalized format."""

        return []

    def fetch_match_stats(self, match_external_id: str) -> dict:
        """Return basic match stats for notification message composition."""

        return {
            "possession_home": 0,
            "possession_away": 0,
            "shots_on_target_home": 0,
            "shots_on_target_away": 0,
        }
