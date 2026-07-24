from task_manager_api.users.schemas import UserResponse
from task_manager_api.users.models import User


def model_to_response(model: User) -> UserResponse:
    return UserResponse(
        id=model.id,
        email=model.email,
        username=model.username,
        admin=model.admin,
        created_at=model.created_at
    )
