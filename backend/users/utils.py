from passlib.context import CryptContext
from database import get_db

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password):
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def commit_refresh(db, model):
    db.add(model)
    db.commit()
    db.refresh(model)