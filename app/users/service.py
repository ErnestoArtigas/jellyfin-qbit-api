from fastapi import HTTPException, status

from .model import User
from . import repository


def get_users() -> list[User]:
    return repository.get_users()


def get_user_by_id(id: str, skip_none_verification=False) -> User | None:
    user = repository.get_user_by_id(id)
    if not user and not skip_none_verification:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found."
        )
    return user


def add_user(user: User) -> User:
    return repository.add_user(user)


def delete_user(id: str) -> None:
    user = get_user_by_id(id)
    return repository.delete_user(user)
