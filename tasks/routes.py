from fastapi import APIRouter, Request
from database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends
from .service import TaskService
from fastapi.responses import HTMLResponse
from templates import templates
import json

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
def get_users(request: Request, db: Session = Depends(get_db)):
    tasks = TaskService(db).get_tasks_with_users()
    return templates.TemplateResponse(request=request, name="index.html", context={"tasks": tasks})
