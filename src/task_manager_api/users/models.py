from datetime import datetime

from sqlalchemy import (
    func,
    text,
    Identity,
    Integer,
    Text,
    Boolean,
    DateTime,
    PrimaryKeyConstraint,
    UniqueConstraint,
    CheckConstraint
)
from sqlalchemy.orm import Mapped, mapped_column

from task_manager_api.database import Base


class User(Base):

    __tablename__="user"
     
    id: Mapped[int] = mapped_column(
        Integer, 
        Identity(always=True, start=1, increment=1)
    )
    username: Mapped[str | None] = mapped_column(Text)
    email: Mapped[str] = mapped_column(Text, nullable=False) 
    hashed_password: Mapped[str] = mapped_column(Text, nullable=False)
    admin: Mapped[bool] = mapped_column(
        Boolean, 
        server_default=text("FALSE"), 
        nullable=False
    )
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime, 
        server_default=func.current_timestamp(), 
        nullable=False
    )
     
    __table_args__ = (
        PrimaryKeyConstraint("id", name="pk_user"),
        UniqueConstraint("username", "email", name="uq_user_email_username"),
        CheckConstraint("username", "username ~ ^[A-Za-z0-9._]+$", name="ck_users_valid_username"),
        CheckConstraint("username", "length(username) >= 8"),
        CheckConstraint("email", "email ~ ^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$", name="ck_email_valid_email")
    )
