from datetime import timedelta
from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from fastapi_jwt_auth import AuthJWT
# from fastapi_jwt_auth.exceptions import AuthJWTException

from .schemas import UserSchema, UserResponseModel, SingleUserResponseModel
from database import get_db
from . import crud
from .utils import verify_password


router = APIRouter(
    prefix="/users",
    tags=["users"]
)


@router.get("/", response_model=List[UserResponseModel])
def test(db: Session = Depends(get_db)):
    users = crud.get_users(db)
    print(users)
    return users


@router.get('/user', response_model=UserResponseModel)
async def user(Authorize: AuthJWT = Depends(), db: Session = Depends(get_db)):
    Authorize.jwt_required()

    current_user = Authorize.get_jwt_subject()

    user = crud.get_user(db, current_user)

    return user


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


@router.post("/login", response_model=SingleUserResponseModel)
def login(user: UserSchema, Authorize: AuthJWT = Depends(), db: Session = Depends(get_db)):
    user_exists = crud.get_user(db, user.username)
    print(user_exists, type(user_exists), user_exists.keys)
    user_exists.test = 'test'
    if not user_exists:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User Not Found")

    if verify_password(user.password, user_exists.password):
        access_token = Authorize.create_access_token(subject=user.username, expires_time=timedelta(days=30))
        refresh_token = Authorize.create_refresh_token(subject=user.username, expires_time=timedelta(days=30))
        return {
                    "access_token": access_token, 
                    "refresh_token": refresh_token,
                    "username": user_exists.username,
                    "role": user_exists.role
               }
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Password do not match")