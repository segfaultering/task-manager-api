from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase

from task_manager_api.config import settings


class Base(DeclarativeBase):
    pass

engine = create_engine(settings.app_db_url, echo=True)
