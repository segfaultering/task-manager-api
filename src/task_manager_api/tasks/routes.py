from typing import Annotated

from fastapi import APIRouter, Depends, status
import sqlalchemy.orm

from task_manager_api.tasks.schemas import (
    TaskCreate,
    TaskUpdate,
    TaskRepr,
    TaskResp
)
from task_manager_api.tasks.services import TaskService
from task_manager_api.utils import get_session, get_current_user_id


router = APIRouter(prefix="/tasks")
DBSession = Annotated[
    sqlalchemy.orm.Session,
    Depends(get_session)
]
CurrUserId = Annotated[
    int, 
    Depends(get_current_user_id)
]


@router.post(
    "/",
    response_model=TaskResp,
    status_code=status.HTTP_201_CREATED
)
def post_task(payload: TaskCreate, session: DBSession, id_: CurrUserId) -> TaskRepr:
    service = TaskService(session, id_) 
    task_repr = service.create(payload)

    return task_repr


@router.get(
    "/",
    response_model=list[TaskResp],
    status_code=status.HTTP_200_OK
)
def get_tasks(session: DBSession, user_id: CurrUserId) -> list[TaskRepr]:
    service = TaskService(session, user_id)
    task_reprs = service.read_all()

    return task_reprs


@router.get(
    "/{id_}/", # Replace with alias "id"
    response_model=TaskResp,
    status_code=status.HTTP_200_OK
)
def get_task(id_: int, session: DBSession, user_id: CurrUserId) -> TaskRepr:
    service = TaskService(session, user_id)
    task_repr = service.read(id_)

    return task_repr


@router.patch(
    "/{id_}/",
    response_model=TaskResp,
    status_code=status.HTTP_200_OK
)
def patch_task(id_: int, payload: TaskUpdate, session: DBSession, user_id: CurrUserId) -> TaskRepr:
    service = TaskService(session, user_id)
    task_repr = service.update(id_, payload)

    return task_repr


@router.delete(
    "/{id_}/",
    response_model=None,
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_task(id_: int, session: DBSession, user_id: CurrUserId) -> None:
    service = TaskService(session, user_id)
    service.delete(id_)

