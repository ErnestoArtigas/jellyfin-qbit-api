from sqlmodel import select
from utils.db_session import DBSession
from .model import PlaybackSession


def get_playback_sessions() -> list[PlaybackSession]:
    with DBSession() as session:
        return session.exec(select(PlaybackSession)).all()


def get_playback_session_by_id(id: str) -> PlaybackSession | None:
    with DBSession() as session:
        return session.exec(
            select(PlaybackSession).where(PlaybackSession.id == id)
        ).first()


def get_playback_session_by_user_id(user_id: str) -> list[PlaybackSession]:
    with DBSession() as session:
        return session.exec(
            select(PlaybackSession).where(PlaybackSession.user_id == user_id)
        ).all()


def add_playback_session(playback_session: PlaybackSession) -> PlaybackSession:
    with DBSession() as session:
        session.add(playback_session)
        session.commit()
        session.refresh(playback_session)
        return playback_session


def delete_playback_session(playback_session: PlaybackSession) -> None:
    with DBSession() as session:
        session.delete(playback_session)
        session.commit()
        return
