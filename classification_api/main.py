from typing import Union
from fastapi import FastAPI

from model.load_model import model

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}