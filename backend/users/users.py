from datetime import timedelta
from typing import List, Union
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from fastapi_jwt_auth import AuthJWT
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

# from fastapi_jwt_auth.exceptions import AuthJWTException

from .schemas import UserSchema, UserResponseModel, UserTokenResponseModel
from database import get_db
from . import crud
from .utils import verify_password


router = APIRouter(
    prefix="/users",
    tags=["users"]
)

security = HTTPBearer()

@router.get("/", response_model=List[UserResponseModel])
def test(db: Session = Depends(get_db)):
    users = crud.get_users(db)
    print(users)
    return users


@router.get('/user', response_model=UserResponseModel)
async def user(Authorize: AuthJWT = Depends(), db: Session = Depends(get_db), credentials: HTTPAuthorizationCredentials = Depends(security)):
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


@router.post("/login", response_model=UserTokenResponseModel)
def login(user: UserSchema, Authorize: AuthJWT = Depends(), db: Session = Depends(get_db)):
    user_exists = crud.get_user(db, user.username)
    if not user_exists:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User Not Found")

    response = user_exists._asdict()

    if verify_password(user.password, user_exists.password):
        access_token = Authorize.create_access_token(subject=user.username, expires_time=timedelta(seconds=30))
        refresh_token = Authorize.create_refresh_token(subject=user.username, expires_time=timedelta(seconds=30))
        response.update({'access_token': access_token, 'refresh_token': refresh_token})
        return response
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Password do not match")


@router.post('/refresh', response_model=UserTokenResponseModel, response_model_exclude_none=True)
def refresh(Authorize: AuthJWT = Depends(), credentials: HTTPAuthorizationCredentials = Depends(security)):
    """
    The jwt_refresh_token_required() function insures a valid refresh
    token is present in the request before running any code below that function.
    we can use the get_jwt_subject() function to get the subject of the refresh
    token, and use the create_access_token() function again to make a new access token
    """
    Authorize.jwt_refresh_token_required()

    current_user = Authorize.get_jwt_subject()
    new_access_token = Authorize.create_access_token(subject=current_user, expires_time=timedelta(days=30))
    return {"access_token": new_access_token}