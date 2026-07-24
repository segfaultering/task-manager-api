from typing import Annotated

from fastapi import APIRouter, Depends, status
import sqlalchemy.orm as orm

from task_manager_api.users.schemas import UserCreate, UserResponse, UserUpdate
from task_manager_api.utils import get_session
import task_manager_api.users.crud as user_crud


type DBSession = Annotated[
    orm.Session,
    Depends(get_session)
]

router = APIRouter()


@router.post(
    "/users/", 
    response_model=UserResponse, 
    status_code=status.HTTP_201_CREATED
)
def post_user(payload: UserCreate, db_session: DBSession) -> UserResponse:
    return user_crud.create_user(payload, db_session)


@router.get(
    "/users/{id}", 
    response_model=UserResponse, 
    status_code=status.HTTP_200_OK
)
def get_user(id: int, db_session: DBSession) -> UserResponse:
    return user_crud.return_user(id, db_session)



@router.get(
    "/users/", 
    response_model=list[UserResponse], 
    status_code=status.HTTP_200_OK
)
def get_users(db_session: DBSession) -> list[UserResponse]:
    return user_crud.return_users(db_session)
    

@router.patch(
    "/users/{id}",
    response_model=UserResponse,
    status_code=status.HTTP_200_OK
)
def edit_users(id: int, payload: UserUpdate, db_session: DBSession) -> UserResponse:
    return user_crud.update_user(id, payload, db_session) 
    

@router.delete(
    "/users/{id}", 
    response_model=None, 
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_user(id: int, db_session: DBSession) -> None:
    user_crud.delete_user(id, db_session)



