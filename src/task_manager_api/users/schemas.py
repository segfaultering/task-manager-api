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
    @classmethod
    def is_valid_username(cls, username: str) -> str:
        valid_chars = string.ascii_letters + string.digits + "_."
        valid = len(set(username)) == len((set(username) & set(valid_chars)))

        if not valid:
            raise ValueError(f"{username} is not a valid username!")

        return username


class UserUpdate(BaseModel):
    email: EmailStr | None = Field(default=None)
    username: str | None = Field(default=None, min_length=8)
    password: str | None = Field(default=None, min_length=8)
    admin: bool | None = Field(default=None)

    @field_validator("password", mode="after")
    @classmethod
    def is_valid_password(cls, passwd: str | None) -> str | None:
        if passwd is None:
            return None

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
    @classmethod
    def is_valid_username(cls, username: str | None) -> str | None:
        if username is None:
            return None

        valid_chars = string.ascii_letters + string.digits + "_."
        valid = len(set(username)) == len((set(username) & set(valid_chars)))

        if not valid:
            raise ValueError(f"{username} is not a valid username!")

        return username


class UserResponse(BaseModel):
    id: PositiveInt
    email: EmailStr
    admin: StrictBool
    created_at: NaiveDatetime
    username: str | None = Field(default=None, min_length=8)

    
    @field_validator("username", mode="after")
    @classmethod
    def is_valid_username(cls, username: str) -> str:
        valid_chars = string.ascii_letters + string.digits + "_."
        valid = len(set(username)) == len((set(username) & set(valid_chars)))

        if not valid:
            raise ValueError(f"{username} is not a valid username!")

        return username

