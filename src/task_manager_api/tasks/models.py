import datetime as dt
import enum

from sqlalchemy import (
    func,
    Integer,
    Identity,
    Text,
    Enum,
    DateTime,
    PrimaryKeyConstraint,
    ForeignKeyConstraint,
    UniqueConstraint,
    CheckConstraint
)
from sqlalchemy.orm import Mapped, mapped_column

from task_manager_api.database import Base


class Status(enum.Enum):
    ONGOING = "ongoing"
    COMPLETE = "complete"
    CANCELLED = "cancelled"


class Task(Base):
    
    __tablename__ = "task"
    
    id: Mapped[int] = mapped_column(
        Integer, 
        Identity(always=True, start=1, increment=1)
    )
    user_id: Mapped[int] = mapped_column(Integer) 
    name: Mapped[str] = mapped_column(Text, nullable=False)
    description: Mapped[str | None] = mapped_column(Text)
    stat: Mapped[Status] = mapped_column(
        Enum(
            Status, 
            values_callable=lambda x: [i.value for i in x]
        ), 
        nullable=False
    )
    created_at: Mapped[dt.datetime] = mapped_column(
        DateTime, 
        server_default=func.current_timestamp(), 
        nullable=False
    )

    __table_args__ = (
        PrimaryKeyConstraint("id", name="pk_task"),
        ForeignKeyConstraint(
            ["user_id"], 
            ["user.id"], 
            name="fk_task_user", 
            onupdate="RESTRICT", 
            ondelete="CASCADE"
        ),
        UniqueConstraint("name", name="uq_task_name"),
        CheckConstraint("length(name) BETWEEN 8 AND 32", name="ck_task_user_username_minlength"),
        CheckConstraint("length(description) >= 8")
    )








