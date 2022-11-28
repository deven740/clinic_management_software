from typing import Dict
from pydantic import BaseModel, Field


class UserSchema(BaseModel):
    username: str = Field(min_length=5)
    password: str = Field(min_length=8)

    class Config:
        orm_mode = True


class UserResponseModel(BaseModel):
    username : str
    role: str

    class Config:
        orm_mode = True