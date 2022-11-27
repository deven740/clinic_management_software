from fastapi import APIRouter, Depends, Request, status, HTTPException
from sqlalchemy.orm import Session
from passlib.context import CryptContext
# from fastapi_jwt_auth import AuthJWT
# from fastapi_jwt_auth.exceptions import AuthJWTException
from fastapi.responses import JSONResponse
from datetime import timedelta

from .models import UserModel, RoleModel
# from .schemas import UserSchema, UserResponseModel
from database import get_db


router = APIRouter(
    prefix="/users",
    tags=["users"]
)


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password):
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


@router.get("/")
async def test(db: Session = Depends(get_db)):
    return db.query(UserModel).all()


# @router.post("/register")
# async def register_user(user: UserSchema, db: Session = Depends(get_db)):
#     user_exists = db.query(UserModel).filter(UserModel.username == user.username).first()
#     if user_exists:
#         raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User Already Exists")
        
#     role = db.query(RoleModel).filter(RoleModel.role == "Supervisor").one()

#     user_model = UserModel()
#     user_model.username = user.username
#     user_model.password = get_password_hash(user.password)
#     user_model.role_id = role.id

#     db.add(user_model)
#     db.commit()

#     return {
#         "status": 201,
#         "transaction": "User Created Successfully"
#     }