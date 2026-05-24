"""Public player-statistics endpoints consumed by the dashboard."""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.players import PlayerCardResponse
from app.services.players import list_active_players

router = APIRouter(prefix="/players")


@router.get("/active", response_model=list[PlayerCardResponse])
def get_active_players(db: Session = Depends(get_db)) -> list[PlayerCardResponse]:
    """Return player cards for active, non-loaned squad members."""

    players = list_active_players(db)
    return [
        PlayerCardResponse(
            id=player.id,
            full_name=player.full_name,
            photo_url=player.photo_url,
            goals_scored=player.goals_scored,
            games_played=player.games_played,
            successful_tackles=player.successful_tackles,
            successful_passes=player.successful_passes,
        )
        for player in players
    ]
