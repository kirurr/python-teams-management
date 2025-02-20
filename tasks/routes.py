from typing import cast
from fastapi import APIRouter, Body, Request, HTTPException
from database import get_db, Task
from sqlalchemy.orm import Session
from fastapi import Depends
from database.schemas import UserTask
from .service import TaskService
from fastapi.responses import HTMLResponse
from templates import templates
from users.service import UsersService
from pydantic import BaseModel


class AddUser(BaseModel):
    user_id: int


router = APIRouter()


@router.get("/", response_class=HTMLResponse)
def get_users(request: Request, db: Session = Depends(get_db)):
    tasks = TaskService(db).get_tasks_with_users()
    users = UsersService(db).get_users()
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"tasks": tasks, "users": users},
    )


@router.delete("/api/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    TaskService(db).delete_task(task_id)


@router.post("/api/tasks/{task_id}")
def add_user(
    task_id: int,
    add_user: AddUser = Body(...),
    db: Session = Depends(get_db),
):
    user_id = cast(int, add_user.model_dump().get("user_id"))
    TaskService(db).add_user(task_id, user_id)


@router.delete("/api/tasks/{task_id}/{user_id}")
def delete_user(task_id: int, user_id: int, db: Session = Depends(get_db)):
    TaskService(db).delete_user(task_id, user_id)


class TaskIn(BaseModel):
    name: str


@router.post("/api/tasks/")
def add_task(task_in: TaskIn = Body(...), db: Session = Depends(get_db)):
    name = task_in.model_dump().get("name")
    if not name:
        raise HTTPException(status_code=400, detail="Task name is required")

    TaskService(db).add_task(name)


@router.put("/api/tasks/{task_id}")
def update_task(
    task_id: int,
    db: Session = Depends(get_db),
    input: TaskIn = Body(...),
):
    name = input.model_dump().get("name")
    if not name:
        raise HTTPException(status_code=400, detail="Task name is required")

    TaskService(db).update_task(task_id, name)
