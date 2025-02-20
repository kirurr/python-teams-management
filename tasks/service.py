from fastapi import HTTPException
from database import Task, UserTask, User
from sqlalchemy.orm import Session


class TaskService:
    def __init__(self, db: Session):
        self.db = db

    def get_tasks_with_users(self):
        tasks = self.db.query(Task)
        users = self.db.query(User)
        users_tasks = self.db.query(UserTask)

        tasks_with_users = []
        for task in tasks:
            task_with_users = {}
            task_with_users["task"] = task.__dict__
            task_with_users["users"] = []

            for user in users_tasks:
                if user.task_id == task.id:
                    task_with_users["users"].append(
                        users.filter(User.id == user.user_id).first().__dict__
                    )
            tasks_with_users.append(task_with_users)
        return tasks_with_users

    def delete_task(self, task_id: int):
        task = self.db.query(Task).filter(Task.id == task_id).first()
        task_users = self.db.query(UserTask).filter(UserTask.task_id == task_id).all()
        if task_users:
            raise HTTPException(status_code=400, detail="Task has users")
        self.db.delete(task)
        self.db.commit()

    def add_user(self, task_id: int, user_id: int):
        task = self.db.query(Task).filter(Task.id == task_id).first()
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")

        user = (
            self.db.query(UserTask)
            .filter(UserTask.user_id == user_id, UserTask.task_id == task_id)
            .first()
        )
        if user:
            raise HTTPException(status_code=400, detail="User already added")

        user_task = UserTask(task_id=task_id, user_id=user_id)
        self.db.add(user_task)
        self.db.commit()

    def delete_user(self, task_id: int, user_id: int):
        user_task = (
            self.db.query(UserTask)
            .filter(UserTask.user_id == user_id, UserTask.task_id == task_id)
            .first()
        )
        if not user_task:
            raise HTTPException(status_code=404, detail="User not found")
        self.db.delete(user_task)
        self.db.commit()

    def add_task(self, name: str):
        task = Task(name=name)
        self.db.add(task)
        self.db.commit()

    def update_task(self, task_id: int, name: str):
        task = self.db.query(Task).filter(Task.id == task_id).first()
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        setattr(task, "name", name)
        self.db.commit()
