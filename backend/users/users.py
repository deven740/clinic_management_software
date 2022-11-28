from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from passlib.context import CryptContext
# from fastapi_jwt_auth import AuthJWT
# from fastapi_jwt_auth.exceptions import AuthJWTException

from .models import UserModel, RoleModel
from .schemas import UserSchema, UserResponseModel
from database import get_db
from . import crud


router = APIRouter(
    prefix="/users",
    tags=["users"]
)


@router.get("/", response_model=List[UserResponseModel])
def test(db: Session = Depends(get_db)):
    users = crud.get_users(db)
    return users


@router.post("/register")
def register_user(user: UserSchema, db: Session = Depends(get_db)):
    user_exists = crud.get_user(db, user.username)
    if user_exists:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User Already Exists")

    user = crud.create_user(db, user=user)        

    return {
        "status": 201,
        "transaction": "User Created Successfully"
    }