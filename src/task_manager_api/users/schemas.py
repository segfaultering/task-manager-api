from pydantic import BaseModel, Field


class UserCreate(BaseModel):
    username: str

class UserResponse(BaseModel):
    id: int = Field(gt=0)
