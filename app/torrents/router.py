from fastapi import APIRouter, status


from . import service

router = APIRouter()


@router.get("/start/", status_code=status.HTTP_204_NO_CONTENT)
def start_torrents(playback_check: bool = False) -> None:
    return service.start_torrents(playback_existence_check=playback_check)


@router.get("/stop/", status_code=status.HTTP_204_NO_CONTENT)
def stop_torrents() -> None:
    return service.stop_torrents()
