import logging
from core.torrents_status import TorrentsStatus
from core.settings import settings
from utils.qbit_client import qbit_client

logger = logging.getLogger("uvicorn.error")


def start_torrents():
    logger.info("Starting torrents.")
    settings.torrents_status = TorrentsStatus.STARTED
    return qbit_client.start_torrents()


def stop_torrents():
    logger.info("Stopping torrents.")
    settings.torrents_status = TorrentsStatus.STOPPED
    return qbit_client.stop_torrents()
