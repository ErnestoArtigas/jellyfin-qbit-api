from fastapi import APIRouter, status

from . import service
from .model import User

router = APIRouter()


@router.get("/", response_model=list[User])
def get_users():
    return service.get_users()


@router.get("/{id}", response_model=User)
def get_user_by_id(id: str):
    return service.get_user_by_id(id)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id: str):
    return service.delete_user(id)
