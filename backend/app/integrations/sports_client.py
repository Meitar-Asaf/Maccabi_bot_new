from dataclasses import dataclass
from datetime import datetime


@dataclass
class GoalEventPayload:
    external_event_id: str
    match_external_id: str
    scorer_name: str
    minute: int
    team_name: str
    event_time: datetime


class SportsClient:
    def fetch_live_goals(self) -> list[GoalEventPayload]:
        return []

    def fetch_match_stats(self, match_external_id: str) -> dict:
        return {
            "possession_home": 0,
            "possession_away": 0,
            "shots_on_target_home": 0,
            "shots_on_target_away": 0,
        }
