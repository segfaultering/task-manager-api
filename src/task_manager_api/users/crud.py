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
        
        if not payload.email is None:
            user.email = payload.email 

        if not payload.username is None:
            user.username = payload.username

        if not payload.admin is None:
            user.admin = payload.admin

        if not payload.password is None:
            user.hashed_password = hash_password(payload.password)  

    return model_to_response(user)


def delete_user(id, dbsession):
    with dbsession.begin():
        user = dbsession.scalars(select(User).where(User.id == id)).one()
        
        if not user:
            raise ValueError(f"user: {id}, to be deleted does not exist!")

        dbsession.delete(user)

     



