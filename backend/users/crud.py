from sqlalchemy.orm import Session

from .models import UserModel
from details.models import DetailsModel, RoleModel, SpecialtyModel
from .schemas import UserSchema
from details.schemas import SpecialtySchema
from .utils import get_password_hash, commit_refresh


def get_user(db: Session, username: str = None):
    return db.query(UserModel.username, UserModel.password).filter(UserModel.username == username).first()


# def get_user_by_email(db: Session, email: str):
#     return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(UserModel.username).all()


def create_user(db: Session, user: UserSchema):
    user.password = get_password_hash(user.password)
    role = db.query(RoleModel).filter(RoleModel.role == user.role).one()

    specialty_model = SpecialtySchema()
    if user.role == 'doctor' and user.specialty:
        result = db.query(SpecialtyModel.specialty, SpecialtyModel.id).filter(SpecialtyModel.specialty == user.specialty).one()
        specialty_model = SpecialtyModel(**result)

    user_model = UserModel(username=user.username, password=user.password)
    commit_refresh(db, user_model)

    details_model = DetailsModel(first_name=user.first_name, last_name=user.last_name, role_id=role.id, user_id=user_model.id, specialty_id=specialty_model.id)
    commit_refresh(db, details_model)

    return user_model


# def get_items(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Item).offset(skip).limit(limit).all()


# def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
#     db_item = models.Item(**item.dict(), owner_id=user_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item
