from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.player import Player


def list_active_players(db: Session) -> list[Player]:
    stmt = (
        select(Player)
        .where(Player.is_active.is_(True), Player.is_loaned_out.is_(False))
        .order_by(Player.full_name.asc())
    )
    return list(db.execute(stmt).scalars().all())
