from fastapi import HTTPException
from sqlalchemy.orm import Session
from database import User, UserTask


class UsersService:
    def __init__(self, db: Session):
        self.db = db

    def get_users(self):
        users = self.db.query(User)
        result = []
        for user in users:
            result.append(user.__dict__)
        return result

    def delete_user(self, user_id: int):
        user = self.db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        user_tasks = self.db.query(UserTask).filter(UserTask.user_id == user_id).all()
        if user_tasks:
            raise HTTPException(status_code=400, detail="User has tasks")

        self.db.delete(user)
        self.db.commit()

    def add_user(self, name: str):
        user = User(name=name)
        self.db.add(user)
        self.db.commit()

    def update_user(self, user_id: int, name: str):
        user = self.db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        setattr(user, "name", name)
        self.db.commit()
