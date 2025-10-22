from utils.jellyfin_client import jellyfin_client
from . import service


def delete_inactive_playback_sessions() -> None:
    playback_sessions = service.get_playback_sessions()
    playback_sessions_to_delete = []
    for playback_session in playback_sessions:
        if not jellyfin_client.is_session_active(id=playback_session.id):
            playback_sessions_to_delete.append(playback_session.id)

    for playback_session_id in playback_sessions_to_delete:
        service.delete_playback_session(id=playback_session_id)
