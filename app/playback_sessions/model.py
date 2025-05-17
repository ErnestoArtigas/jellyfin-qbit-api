from datetime import datetime, timezone
from typing import TYPE_CHECKING, Optional
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from users.model import User


class PlaybackSession(SQLModel, table=True):
    id: Optional[str] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    user_id: Optional[str] = Field(
        default=None, foreign_key="user.id", ondelete="CASCADE"
    )
    user: Optional["User"] = Relationship(back_populates="playback_sessions")
