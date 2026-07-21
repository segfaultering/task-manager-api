from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from task_manager_api.config import settings


class Base(DeclarativeBase):
    pass

engine = create_engine(settings.app_db_url, echo=True)

SessionLocal = sessionmaker(engine, expire_on_commit=False)
