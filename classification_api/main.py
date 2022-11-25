from typing import Union
from fastapi import FastAPI, UploadFile
from time import sleep
import asyncio

from model import classify

app = FastAPI()

app.include_router(classify.router)

@app.get("/")
async def read_root():
    return {"Hello": "World"}


