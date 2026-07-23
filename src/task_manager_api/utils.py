from pwdlib import PasswordHash
from pwdlib.hashers.argon2 import Argon2Hasher

from task_manager_api.database import SessionLocal


def get_session():
    with SessionLocal() as session:
        yield session

def hash_password(password: str) -> str:
    hasher = PasswordHash((Argon2Hasher(),))
    return hasher.hash(password)

      
