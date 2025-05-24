from pydantic import computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict

from .torrents_status import TorrentsStatus


class Settings(BaseSettings):
    qbittorrent_api_endpoint: str
    qbittorrent_api_user: str
    qbittorrent_api_password: str

    _torrents_status: TorrentsStatus = TorrentsStatus.STOPPED

    @computed_field
    @property
    def torrents_status(self) -> TorrentsStatus:
        return self._torrents_status

    @torrents_status.setter
    def torrents_status(self, new_torrents_status: TorrentsStatus) -> None:
        self._torrents_status = new_torrents_status

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
