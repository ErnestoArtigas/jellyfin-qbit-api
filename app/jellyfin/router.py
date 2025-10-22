from fastapi import APIRouter, status

from playback_sessions.job import delete_inactive_playback_sessions


from . import service

router = APIRouter()


@router.get("/sessions/{id}", status_code=status.HTTP_200_OK)
def is_session_active(id: str) -> None:
    return delete_inactive_playback_sessions()
