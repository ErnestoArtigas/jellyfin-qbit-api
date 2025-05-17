import qbittorrentapi

from core.settings import settings


class QbitClient:
    _api_client: qbittorrentapi.Client

    def __init__(self):
        self._api_client = qbittorrentapi.Client(
            **dict(
                host=settings.qbittorrent_api_endpoint,
                username=settings.qbittorrent_api_user,
                password=settings.qbittorrent_api_password,
            )
        )

    def login(self) -> None:
        try:
            self._api_client.auth_log_in()
        except qbittorrentapi.LoginFailed as err:
            print(f"LoginFailed {err}")

    def start_torrents(self) -> None:
        self._api_client.torrents.start.all()

    def stop_torrents(self) -> None:
        self._api_client.torrents.stop.all()


qbit_client = QbitClient()
