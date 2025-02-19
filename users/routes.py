from fastapi import APIRouter
from .service import UsersService
from database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends

router = APIRouter()


@router.get("/users")
def get_users(db: Session = Depends(get_db)):
    return UsersService(db).test()
