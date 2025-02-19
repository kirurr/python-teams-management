from fastapi import FastAPI
from users.routes import router as users_router
from database import engine, Base


app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(users_router)

