import logging
from utils.qbit_client import qbit_client

from playback_sessions import service as playback_sessions_service

logger = logging.getLogger("uvicorn.error")


def start_torrents(playback_existence_check: bool = False) -> None:
    logger.info("Starting torrents.")

    if (
        playback_existence_check
        and not len(playback_sessions_service.get_playback_sessions()) == 0
    ):
        return None
    return qbit_client.start_torrents()


def stop_torrents() -> None:
    logger.info("Stopping torrents.")
    return qbit_client.stop_torrents()
