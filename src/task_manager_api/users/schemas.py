import string

from pydantic import (
    BaseModel, 
    Field, 
    EmailStr,
    StrictBool,
    PositiveInt, 
    NaiveDatetime,
    field_validator
)


class UserCreate(BaseModel):
    admin: StrictBool = Field(default=False)
    password: str = Field(min_length=8) 
    email: EmailStr
    username: str | None = Field(default=None, min_length=8)

    @field_validator("password", mode="after")
    @classmethod
    def is_valid_password(cls, passwd: str) -> str:
        valid_format = (
            (passwd in string.ascii_uppercase) and 
            (passwd in string.ascii_lowercase) and
            (passwd in string.digits) and
            (passwd in string.punctuation)
        )

        if not valid_format:
            ValueError(f"{passwd} is not a valid password!")

        return passwd
         
    @field_validator("username", mode="after")
    @property
    def is_valid_username(cls, username: str) -> str:
        valid_chars = string.ascii_letters + string.digits + "_."

        if not (username in valid_chars):
            raise ValueError(f"{username} is not a valid username!")

        return username

class UserResponse(BaseModel):
    id: PositiveInt
    email: EmailStr
    admin: StrictBool
    created_at: NaiveDatetime
    username: str | None = Field(default=None, min_length=8)

    
    @field_validator("username", mode="after")
    @property
    def is_valid_username(cls, username: str) -> str:
        valid_chars = string.ascii_letters + string.digits + "_."

        if not (username in valid_chars):
            raise ValueError(f"{username} is not a valid username!")

        return username
