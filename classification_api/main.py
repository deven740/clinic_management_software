from typing import Union
from fastapi import FastAPI, UploadFile
from time import sleep
import asyncio

from model.load_model import model
from model.classify import predict

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
        # convert that to bytes
    image_bytes = await file.read()
    predict(image_bytes=image_bytes)
    # await asyncio.sleep(5)
    return {"filename": file.filename}