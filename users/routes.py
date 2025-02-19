from fastapi import APIRouter
from .repository import UsersRepository

router = APIRouter()


@router.get("/users")
def get_users():
    return UsersRepository().test()
