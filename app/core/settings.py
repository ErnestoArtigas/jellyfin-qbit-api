from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    jellyfin_api_endpoint: str
    jellyfin_api_key: str
    qbittorrent_api_endpoint: str
    qbittorrent_api_user: str
    qbittorrent_api_password: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()  # type: ignore
