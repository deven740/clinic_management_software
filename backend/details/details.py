from datetime import timedelta
from typing import List, Union
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from . import crud
from .schemas import SpecialtyResponseModel, DoctorSpecialtyResponseModel


router = APIRouter(
    prefix="/specialty",
    tags=["specialty"]
)


@router.get("/", response_model=List[SpecialtyResponseModel])
def get_specialty(db: Session = Depends(get_db)):
    specialty = crud.get_specialty(db)
    return specialty
    

@router.get("/filter-doctors-by-specialty", response_model=List[DoctorSpecialtyResponseModel])
def filter_doctors_by_specialty(db: Session = Depends(get_db), specialty: str | None = None):
    result = crud.filter_doctors_by_specialty(db, specialty)
    return result