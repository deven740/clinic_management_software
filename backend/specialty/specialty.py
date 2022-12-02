from datetime import timedelta
from typing import List, Union
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from . import crud
from .schemas import SpecialtyResponseModel


router = APIRouter(
    prefix="/specialty",
    tags=["specialty"]
)


@router.get("/", response_model=List[SpecialtyResponseModel])
def test(db: Session = Depends(get_db)):
    specialty = crud.get_specialty(db)
    print(specialty)
    return specialty

