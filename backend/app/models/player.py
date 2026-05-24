from datetime import datetime
from uuid import uuid4

from sqlalchemy import Boolean, DateTime, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class Player(Base):
    __tablename__ = "players"

    id: Mapped[str] = mapped_column(UUID(as_uuid=False), primary_key=True, default=lambda: str(uuid4()))
    external_player_id: Mapped[str] = mapped_column(String(64), unique=True, index=True)
    full_name: Mapped[str] = mapped_column(String(150), index=True)
    short_name: Mapped[str | None] = mapped_column(String(80), nullable=True)
    shirt_number: Mapped[int | None] = mapped_column(Integer, nullable=True)
    position: Mapped[str] = mapped_column(String(40))
    photo_url: Mapped[str | None] = mapped_column(String(500), nullable=True)
    team_name: Mapped[str] = mapped_column(String(120), default="Maccabi Tel Aviv")
    parent_club: Mapped[str | None] = mapped_column(String(120), nullable=True)
    current_club: Mapped[str] = mapped_column(String(120), default="Maccabi Tel Aviv")
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, index=True)
    is_loaned_out: Mapped[bool] = mapped_column(Boolean, default=False, index=True)
    season: Mapped[str] = mapped_column(String(12), index=True)
    games_played: Mapped[int] = mapped_column(Integer, default=0)
    goals_scored: Mapped[int] = mapped_column(Integer, default=0)
    successful_tackles: Mapped[int] = mapped_column(Integer, default=0)
    successful_passes: Mapped[int] = mapped_column(Integer, default=0)
    source_updated_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow)
