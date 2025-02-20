from fastapi import APIRouter, HTTPException, Body
from pydantic import BaseModel
from database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends

from users.service import UsersService

router = APIRouter()


@router.delete("/api/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    UsersService(db).delete_user(user_id)


class UserIn(BaseModel):
    name: str


@router.post("/api/users/")
def add_user(db: Session = Depends(get_db), input: UserIn = Body(...)):
    name = input.model_dump().get("name")
    if not name:
        raise HTTPException(status_code=400, detail="User name is required")

    UsersService(db).add_user(name)


@router.put("/api/users/{user_id}")
def update_user(
    user_id: int,
    db: Session = Depends(get_db),
    input: UserIn = Body(...),
):
    name = input.model_dump().get("name")
    if not name:
        raise HTTPException(status_code=400, detail="User name is required")

    UsersService(db).update_user(user_id, name)
