from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    relationship,
    mapped_column,
)

from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    user_tasks = relationship("UserTask", back_populates="user")

class Task(Base):
    __tablename__ = "task"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    user_tasks = relationship("UserTask", back_populates="task")

class UserTask(Base):
    __tablename__ = "user_task"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("user.id"))
    user: Mapped[User] = relationship(User, back_populates="user_tasks")
    task_id: Mapped[int] = mapped_column(Integer, ForeignKey("task.id"))
    task: Mapped[Task] = relationship(Task, back_populates="user_tasks")
