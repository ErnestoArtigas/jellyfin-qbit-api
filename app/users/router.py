from fastapi import APIRouter, status

from utils.qbit_client import qbit_client

from . import service
from .model import User

from playback_sessions import service as playback_sessions_service

router = APIRouter()


@router.get("/", response_model=list[User])
def get_users():
    return service.get_users()


@router.get("/{id}", response_model=User)
def get_user_by_id(id: str):
    return service.get_user_by_id(id)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id: str):
    service.delete_user(id)
    playback_sessions = playback_sessions_service.get_playback_sessions()
    if len(playback_sessions) == 0:
        qbit_client.start_torrents()
    return None
