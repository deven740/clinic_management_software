from sqlalchemy.orm import Session

from .models import UserModel, RoleModel
from .schemas import UserSchema
from .utils import get_password_hash


def get_user(db: Session, username: str = None):
    return db.query(UserModel.username, UserModel.password, RoleModel.role).join(RoleModel).filter(UserModel.username == username).first()


# def get_user_by_email(db: Session, email: str):
#     return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(UserModel.username, RoleModel.role).join(RoleModel).offset(skip).limit(limit).all()


def create_user(db: Session, user: UserSchema):
    user.password = get_password_hash(user.password)
    role = db.query(RoleModel).filter(RoleModel.role == "patient").one()
    user_model = UserModel(**user.dict(), role_id=role.id)

    db.add(user_model)
    db.commit()
    db.refresh(user_model)
    return user_model


# def get_items(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Item).offset(skip).limit(limit).all()


# def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
#     db_item = models.Item(**item.dict(), owner_id=user_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item
