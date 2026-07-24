from sqlalchemy import select

from task_manager_api.utils import hash_password
from task_manager_api.users.schemas import UserResponse, UserCreate
from task_manager_api.users.models import User
from task_manager_api.users.utils import model_to_response



def create_user(payload: UserCreate, dbsession) -> UserResponse:
    with dbsession.begin():
        user = User(
            email=payload.email,
            username=payload.username,
            admin=payload.admin,
            hashed_password=hash_password(payload.password)
        )

        dbsession.add(user)
    
    return model_to_response(user)

def return_user(id, dbsession):
    with dbsession.begin():
        user = dbsession.scalars(select(User).where(User.id == id)).one()

    return model_to_response(user) 


def return_users(dbsession):
    with dbsession.begin():
        users = dbsession.scalars(select(User)).all()

    return [model_to_response(user) for user in users]


def update_user(id, payload, dbsession):
    with dbsession.begin():
        user = dbsession.scalars(select(User).where(User.id == id)).one()
        
        if payload.email is not None:
            user.email = payload.email 

        if payload.username is not None:
            user.username = payload.username

        if payload.admin is not None:
            user.admin = payload.admin

        if payload.password is not None:
            user.hashed_password = hash_password(payload.password)  

    return model_to_response(user)


def delete_user(id, dbsession):
    with dbsession.begin():
        user = dbsession.scalars(select(User).where(User.id == id)).one()
        
        if not user:
            raise ValueError(f"user: {id}, to be deleted does not exist!")

        dbsession.delete(user)

     



