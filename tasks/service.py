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
                    task_with_users["users"].append(users.filter(User.id == user.user_id).first().__dict__)
            tasks_with_users.append(task_with_users)
        return tasks_with_users
