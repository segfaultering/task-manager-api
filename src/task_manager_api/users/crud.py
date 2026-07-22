from sqlalchemy import select

from task_manager_api.users.schemas import UserResponse
from task_manager_api.users.models import User


def create_user(username, session):
    user = User(username=username)
    with session.begin():
        session.add(user)
    
    return UserResponse(id=user.id, username=user.username)

def return_user(id, session):
    with session.begin():
        user = session.scalars(select(User).where(User.id == id)).one()

    
    return UserResponse(id=user.id, username=user.username)


