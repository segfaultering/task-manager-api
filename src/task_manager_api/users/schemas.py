from pydantic import (
    BaseModel, 
    Field, 
    EmailStr,
    StrictBool,
    PositiveInt, 
    NaiveDatetime
)


class UserCreate(BaseModel):
    username: str

class UserResponse(BaseModel):
    id: PositiveInt
    email: EmailStr
    admin: StrictBool
    created_at: NaiveDatetime
    username: str | None = Field(
        default=None,
        min_length=8,
        pattern="^[A-Za-z0-9_.]$"
    )
