from contextlib import closing

from task_manager_api.database import SessionLocal


def get_session():
    with SessionLocal() as session:
        yield session
