from fastapi import FastAPI
from users import users

app = FastAPI()

app.include_router(users.router)


@app.get("/")
async def read_root():
    return {"Hello": "World"}