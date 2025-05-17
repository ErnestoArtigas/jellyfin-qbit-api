from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    qbittorrent_api_endpoint: str
    qbittorrent_api_user: str
    qbittorrent_api_password: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
