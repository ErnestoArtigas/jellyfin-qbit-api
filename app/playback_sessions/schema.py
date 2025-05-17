from pydantic import BaseModel


class PlaybackSessionMediaSource(BaseModel):
    Id: str
    Path: str


class PlaybackSessionPublic(BaseModel):
    UserId: str
    UserName: str
    SessionId: str
    MediaSource: PlaybackSessionMediaSource | None = None
