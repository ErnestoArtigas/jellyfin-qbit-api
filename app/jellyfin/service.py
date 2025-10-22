from utils.jellyfin_client import jellyfin_client


def is_session_active(id: str) -> bool:
    return jellyfin_client.is_session_active(id)
