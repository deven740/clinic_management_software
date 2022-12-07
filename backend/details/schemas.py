from typing import Dict
from pydantic import BaseModel, Field, validator


class SpecialtyResponseModel(BaseModel):
    id: int
    specialty : str

    class Config:
        orm_mode = True


class SpecialtySchema(BaseModel):
    id: int = None
    specialty : str = None

    class Config:
        orm_mode = True


class DoctorSpecialtyResponseModel(BaseModel):
    full_name: str
    id: int