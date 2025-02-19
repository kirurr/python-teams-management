from fastapi import FastAPI
from users.routes import router as users_router
from tasks.routes import router as tasks_router
from database import engine, Base
from fastapi.staticfiles import StaticFiles

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(users_router)
app.include_router(tasks_router)
