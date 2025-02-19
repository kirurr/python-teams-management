from sqlalchemy.orm import Session
from database import User


class UsersService:
    def __init__(self, db: Session):
        self.db = db

    def get_users(self):
        return self.db.query(User).all()
