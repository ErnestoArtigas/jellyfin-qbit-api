from datetime import datetime, timezone
from typing import TYPE_CHECKING, Optional
from sqlmodel import Field, Relationship, SQLModel, func
from sqlalchemy import event, inspect

from torrents import service as torrents_service

if TYPE_CHECKING:
    from users.model import User


class PlaybackSession(SQLModel, table=True):
    id: Optional[str] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    user_id: Optional[str] = Field(
        default=None, foreign_key="user.id", ondelete="CASCADE"
    )
    user: Optional["User"] = Relationship(back_populates="playback_sessions")


@event.listens_for(PlaybackSession, "before_insert")
def stopping_torrents_before_insert(_mapper, _connection, target):
    session = inspect(target).session
    length_playback_session = session.exec(func.count(PlaybackSession.id)).scalar()
    if length_playback_session == 0:
        torrents_service.stop_torrents()


@event.listens_for(PlaybackSession, "after_delete")
def starting_torrents_before_insert(_mapper, _connection, target):
    session = inspect(target).session
    length_playback_session = session.exec(func.count(PlaybackSession.id)).scalar()
    if length_playback_session == 0:
        torrents_service.start_torrents()
