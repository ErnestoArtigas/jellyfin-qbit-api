from typing import TYPE_CHECKING, Optional
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from playback_sessions.model import PlaybackSession


class User(SQLModel, table=True):
    id: Optional[str] = Field(default=None, primary_key=True)
    name: str

    playback_sessions: list["PlaybackSession"] = Relationship(
        back_populates="user", cascade_delete=True
    )
