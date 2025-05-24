from pydantic import BaseModel


class PlaybackSessionPublic(BaseModel):
    UserId: str
    UserName: str
    SessionId: str
