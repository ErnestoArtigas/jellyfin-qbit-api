from fastapi import APIRouter, status


from . import service
from .model import PlaybackSession
from .schema import PlaybackSessionPublic

router = APIRouter()


@router.get("/", response_model=list[PlaybackSession])
def get_playback_sessions():
    return service.get_playback_sessions()


@router.get("/{id}", response_model=PlaybackSession)
def get_playback_session_by_id(id: str):
    return service.get_playback_session_by_id(id)


@router.get("/user/{id}", response_model=list[PlaybackSession])
def get_playback_session_by_user_id(user_id: str):
    return service.get_playback_session_by_user_id(user_id)


@router.post("/", response_model=PlaybackSession)
def create_playback_session(
    playback_session_public: PlaybackSessionPublic,
):
    return service.create_playback_session(playback_session_public)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_playback_session(id: str):
    return service.delete_playback_session(id)
