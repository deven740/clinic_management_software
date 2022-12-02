from sqlalchemy.orm import Session
from .models import SpecialtyModel


def get_specialty(db: Session, specialty: str = None):
    return db.query(SpecialtyModel).all()