from typing import Protocol

from sqlalchemy import select
import sqlalchemy.orm as orm

from task_manager_api.tasks.schemas import (
    Create, 
    Update, 
    Representation,
    TaskCreate, 
    TaskUpdate,
    TaskRepr
)
from task_manager_api.tasks.models import Task, Status


class Service(Protocol):
    def create(self, payload: Create) -> Representation: 
        ...

    def read(self, id_: int) -> Representation: 
        ...

    def read_all(self) -> list[Representation]: 
        ...

    def update(self, id_: int, payload: Update) -> Representation: 
        ...

    def delete(self, id_: int) -> None: 
        ...


class TaskService:
    def __init__(self, session: orm.Session, curr_user_id: int) -> None:
        self.session = session 
        self.user_id = curr_user_id 
    
    def create(self, payload: TaskCreate) -> TaskRepr:
        with self.session.begin():
            task = Task(
                user_id=self.user_id,
                name=payload.name,
                description=payload.description,
                stat=Status.ONGOING.value
            )

            self.session.add(task)

        return TaskRepr.model_validate(task)
            
    def read(self, id_: int) -> TaskRepr:
        # I should test out what inputting invalid ids will result in in terms of an error
        with self.session.begin():
            stmt = (
                select(Task)
                .where(
                    Task.id == id_,
                    Task.user_id == self.user_id
                )
            )

            task = self.session.scalars(stmt).one()
 
        return TaskRepr.model_validate(task)

    def read_all(self) -> list[TaskRepr]:
        with self.session.begin():
            stmt = (
                select(Task)
                .where(Task.user_id == self.user_id)
            )

            tasks = self.session.scalars(stmt).all()

        return [TaskRepr.model_validate(task) for task in tasks]


    def update(self, id_: int, payload: TaskUpdate) -> TaskRepr:
        with self.session.begin():
            stmt = (
                select(Task)
                .where(
                    Task.id == id_,
                    Task.user_id == self.user_id
                )
            )

            task = self.session.scalars(stmt).one()

            if payload.name:
                task.name = payload.name

            if payload.description:
                task.description = payload.description

            if payload.stat:
                task.stat = payload.stat

        return TaskRepr.model_validate(task)


    def delete(self, id_: int) -> None:
        with self.session.begin():
            stmt = (
                select(Task)
                .where(
                    Task.id == id_,
                    Task.user_id == self.user_id
                )
            )

            task = self.session.scalars(stmt).one()
            self.session.delete(task)

          






