import logging
from utils.qbit_client import qbit_client

logger = logging.getLogger("uvicorn.error")


def start_torrents():
    logger.info("Starting torrents.")
    return qbit_client.start_torrents()


def stop_torrents():
    logger.info("Stopping torrents.")
    return qbit_client.stop_torrents()
