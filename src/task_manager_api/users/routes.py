from typing import Annotated

from fastapi import APIRouter, Depends
import sqlalchemy.orm as orm

from task_manager_api.users.schemas import UserCreate, UserResponse
from task_manager_api.utils import get_session
import task_manager_api.users.crud as user_crud


type DBSession = Annotated[
    orm.Session,
    Depends(get_session)
]

router = APIRouter()

@router.post("/users/", response_model=UserResponse)
def post_user(payload: UserCreate, db_session: DBSession) -> UserResponse:
    return user_crud.create_user(payload, db_session)


@router.get("/users/{id}", response_model=UserResponse)
def get_user(id: int, db_session: DBSession) -> UserResponse:
    return user_crud.return_user(id, db_session)


@router.get("/users/", response_model=list[UserResponse])
def get_users(db_session: DBSession) -> list[UserResponse]:
    return user_crud.return_users(db_session)
    




