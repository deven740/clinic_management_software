from fastapi import FastAPI
from users import users
from details import details
import auth
from fastapi_jwt_auth.exceptions import AuthJWTException
from fastapi.middleware.cors import CORSMiddleware
from database import Base, engine

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(details.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}


app.add_exception_handler(AuthJWTException, auth.authjwt_exception_handler)

Base.metadata.create_all(bind=engine)

