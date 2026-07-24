from typing import Protocol
from collections.abc import Iterable

from sqlalchemy import select
import sqlalchemy.orm.Session as DBSession
from pydantic import BaseModel

from task_manager_api.tasks.schemas import (
    Create, 
    Update, 
    Delete, 
    Representation,
    TaskCreate, 
    TaskUpdate,
    TaskDelete,
    TaskRepr,
    TaskResp
)
from task_manager_api.tasks.models import Task


class Service(Protocol):
    def create(self, payload: Create) -> Representation: 
        ...

    def read(self, id_: int) -> Representation: 
        ...

    def read(self) -> list[Representation]: 
        ...

    def update(self, id_: int, payload: Update) -> Representation: 
        ...

    def delete(self, id_: int) -> None: 
        ...


class TaskService:
    def __init__(self, session: DBSession, curr_user_id: int) -> None:
        self.session = session 
        self.user_id = curr_user_id 
    
    def create(self, payload: TaskCreate) -> TaskRepr:
        with self.session.begin() as session:
            task = Task(
                user_id=self.user_id,
                name=payload.name,
                description=payload.description
            )

            session.add(task)

        return TaskRepr.model_validate(task)
            
    def read(self, id_: int) -> TaskRepr:
        # I should test out what inputting invalid ids will result in in terms of an error
        with self.session.begin() as session:
            stmt = (
                select(Task)
                .where(
                    Task.id == id_,
                    Task.user_id == self.user_id
                )
            )

            task = session.scalars(stmt).one()
 
        return TaskRepr.model_validate(task)

    def read(self) -> list[TaskRepr]:
        with self.session.begin() as session:
            stmt = (
                select(Task)
                .where(Task.user_id = self.user_id)
            )

            tasks = session.scalars(stmt).all()

        return [TaskRepr.model_validate(task) for task in tasks]


    def update(self, id_: int, payload: TaskUpdate) -> TaskRepr:
        with self.session.begin() as session:
            stmt = (
                select(Task)
                .where(
                    Task.id == id_,
                    Task.user_id == self.user_id
                )
            )

            task = session.scalars(stmt).one()

            if payload.name:
                task.name = payload.name

            if payload.description:
                task.description = payload.description

            if payload.stat:
                task.stat = payload.stat

        return TaskRepr.model_validate(task)


    def delete(self, id_: int) -> None:
        with self.session.begin() as session:
            stmt = (
                select(Task)
                .where(
                    Task.id == id_,
                    Task.user_id == self.user_id
                )
            )

            task = session.scalars(stmt).one()
            session.delete(task)

        






