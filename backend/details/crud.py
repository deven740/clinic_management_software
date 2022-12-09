from sqlalchemy.orm import Session
from .models import SpecialtyModel, RoleModel, DetailsModel
from users.models import UserModel


def get_specialty(db: Session, specialty: str = None):
    return db.query(SpecialtyModel).all()


def get_roles(db: Session, role: str = None):
    return db.query(RoleModel).all()


def filter_doctors_by_specialty(db: Session, specialty: str = None):
    result =  db.query(DetailsModel.full_name, SpecialtyModel.id.label("specialty_id"), DetailsModel.id.label("details_id")).join(SpecialtyModel)
    if specialty:
        return result.filter(SpecialtyModel.specialty == specialty).all()
    return result.all()