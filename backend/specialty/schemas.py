from typing import Dict
from pydantic import BaseModel, Field


class SpecialtyResponseModel(BaseModel):
    id: int
    specialty : str

    class Config:
        orm_mode = True


