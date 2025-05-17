from fastapi import HTTPException, status

from playback_sessions.schema import PlaybackSessionPublic

from .model import PlaybackSession
from . import repository

from users import service as users_service
from users.model import User


def get_playback_sessions() -> list[PlaybackSession]:
    return repository.get_playback_sessions()


def get_playback_session_by_id(
    id: str, skip_none_verification=False
) -> PlaybackSession | None:
    playback_session = repository.get_playback_session_by_id(id)
    if not playback_session and not skip_none_verification:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="PlaybackSession not found."
        )
    return playback_session


def get_playback_session_by_user_id(user_id: str) -> list[PlaybackSession]:
    return repository.get_playback_session_by_user_id(user_id)


def add_playback_session(playback_session: PlaybackSession) -> PlaybackSession:
    existing_playback_session = repository.get_playback_session_by_id(
        playback_session.id
    )
    if existing_playback_session:
        return existing_playback_session
    return repository.add_playback_session(playback_session)


def create_playback_session(
    playback_session_public: PlaybackSessionPublic,
) -> PlaybackSession:
    user = users_service.get_user_by_id(
        playback_session_public.UserId, skip_none_verification=True
    )
    if not user:
        user = users_service.add_user(
            User(
                id=playback_session_public.UserId, name=playback_session_public.UserName
            )
        )
    playback_session = PlaybackSession(
        id=playback_session_public.SessionId,
        user_id=playback_session_public.UserId,
    )
    return add_playback_session(playback_session)


def delete_playback_session(id: str) -> None:
    playback_session = get_playback_session_by_id(id)
    return repository.delete_playback_session(playback_session)
