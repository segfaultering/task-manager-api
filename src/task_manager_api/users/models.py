from sqlalchemy import (
    Identity,
    Integer,
    Mapped,
    mapped_column
    PrimaryKeyConstraint
)

from task_manager_api.database import Base


class User(Base):

    __tablename__="user"
     
    id: Mapped[int] = mapped_column(Integer, Identity(start=1, increment=1))

    PrimaryKeyConstraint("id", name="pk_user")
