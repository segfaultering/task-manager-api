from sqlalchemy import (
    Identity,
    Integer,
    Text,
    Mapped,
    mapped_column
    PrimaryKeyConstraint
)

from task_manager_api.database import Base


class User(Base):

    __tablename__="user"
     
    id: Mapped[int] = mapped_column(Integer, Identity(start=1, increment=1))
    username: Mapped[str] = mapped_column(Text, nullable=False)

    PrimaryKeyConstraint("id", name="pk_user")
