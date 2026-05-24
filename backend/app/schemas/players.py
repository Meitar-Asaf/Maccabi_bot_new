"""Pydantic schemas for player card responses."""

from pydantic import BaseModel


class PlayerCardResponse(BaseModel):
    """Serialized player stats used by the frontend player cards."""

    id: str
    full_name: str
    photo_url: str | None
    goals_scored: int
    games_played: int
    successful_tackles: int
    successful_passes: int
