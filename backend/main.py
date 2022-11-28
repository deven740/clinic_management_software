from fastapi import FastAPI
from users import users
import auth
from fastapi_jwt_auth.exceptions import AuthJWTException


app = FastAPI()

app.include_router(users.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}


app.add_exception_handler(AuthJWTException, auth.authjwt_exception_handler)

