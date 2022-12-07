from typing import Dict, Literal
from pydantic import BaseModel, Field


class UserSchema(BaseModel):
    username: str = Field(min_length=5)
    password: str = Field(min_length=8)
    first_name: str
    last_name: str
    role: Literal['patient', 'doctor', 'receptionist']
    specialty: str = None

    class Config:
        orm_mode = True


class UserResponseModel(BaseModel):
    username : str
    # role: str
    class Config:
        orm_mode = True


class UserTokenResponseModel(UserResponseModel):
    access_token : str
    refresh_token : str

    class Config:
        orm_mode = True
