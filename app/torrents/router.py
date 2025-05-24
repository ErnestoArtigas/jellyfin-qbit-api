from fastapi import APIRouter, status

from core.torrents_status import TorrentsStatus
from core.settings import settings


from . import service

router = APIRouter()


@router.get("/start", status_code=status.HTTP_204_NO_CONTENT)
def start_torrents():
    return service.start_torrents()


@router.get("/stop", status_code=status.HTTP_204_NO_CONTENT)
def stop_torrents():
    return service.stop_torrents()


@router.get("/status", response_model=TorrentsStatus)
def status_torrents():
    return settings.torrents_status
