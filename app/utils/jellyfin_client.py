import httpx
from core.settings import settings


class JellyfinClient:
    _api_endpoint: str
    _api_key: str

    def __init__(self) -> None:
        self._api_endpoint = settings.jellyfin_api_endpoint
        self._api_key = settings.jellyfin_api_key

    def get_all_sessions(self) -> list:
        sessions = httpx.get(
            url=f"{self._api_endpoint}/Sessions/",
            headers={"Authorization": f'MediaBrowser Token="{self._api_key}"'},
        )
        return sessions.json()

    def is_session_active(self, id: str) -> bool:
        sessions = self.get_all_sessions()
        return any(
            id == session["Id"] and session["PlayState"]["CanSeek"]
            for session in sessions
        )


jellyfin_client = JellyfinClient()
