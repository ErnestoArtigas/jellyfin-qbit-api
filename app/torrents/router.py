from fastapi import APIRouter, status


from . import service

router = APIRouter()


@router.get("/start", status_code=status.HTTP_204_NO_CONTENT)
def start_torrents():
    return service.start_torrents()


@router.get("/stop", status_code=status.HTTP_204_NO_CONTENT)
def stop_torrents():
    return service.stop_torrents()
