from typing import Annotated

from fastapi import APIRouter, Depends
import sqlalchemy

from task_manager_api.users.schemas import UserCreate, UserResponse
from task_manager_api.users.crud import create_user, return_user
from task_manager_api.utils import get_session


type Engine = Annotated[
    sqlalchemy.engine.Engine,
    Depends(get_session)
]


router = APIRouter()

@router.post("/users/", response_model=UserResponse)
def post_user(payload: UserCreate, engine: Engine) -> UserResponse:
    return create_user(payload.username, engine)


@router.get("/users/{id}", response_model=UserResponse)
def get_user(id: int, engine: Engine) -> UserResponse:
    return return_user(id, engine)



