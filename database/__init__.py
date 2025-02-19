from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .schemas import (
    Base,
    User,
    Task,
    UserTask,
)

DATABASE_URL = "db/teams.db"

engine = create_engine(f"sqlite:///{DATABASE_URL}")
SessionLocal = sessionmaker(autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
