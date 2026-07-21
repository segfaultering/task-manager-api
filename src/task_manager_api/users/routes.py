from typing import Annotated

from fastapi import Router, Depends
import sqlalchemy
from sqlalchemy import select

from task_manager_api.users.schemas import UserCreate, UserResponse
from task_manager_api.useres.crud import create_user, get_user
from task_manager_api.utils import get_session


type Engine = Annotated[
    sqlalchemy._engine.Engine,
    Depends(get_session)
]


router = Router()

@router.post("/users/", response_model=UserResponse)
def post_user(payload: UserCreate, engine: Engine) -> UserResponse:
    return create_user(payload.username, engine)


@router.get("/users/{id}", response_model=UserResponse):
def get_user(id: int, engine: Engine) -> UserResponse:
    return get_all(id, engine)



