from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .schemas import Teams

DATABASE_URL = "sqlite:///db/teams.db"

engine = create_engine(f"sqlite:///{DATABASE_URL}")
SessionLocal = sessionmaker(engine)
