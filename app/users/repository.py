from sqlmodel import select
from utils.db_session import DBSession
from .model import User


def get_users() -> list[User]:
    with DBSession() as session:
        return session.exec(select(User)).all()


def get_user_by_id(id: str) -> User | None:
    with DBSession() as session:
        return session.exec(select(User).where(User.id == id)).first()


def add_user(user: User) -> User:
    with DBSession() as session:
        session.add(user)
        session.commit()
        session.refresh(user)
        return user


def delete_user(user: User) -> None:
    with DBSession() as session:
        session.delete(user)
        session.commit()
        return
