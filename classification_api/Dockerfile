FROM pytorch/pytorch:1.8.1-cuda11.1-cudnn8-runtime
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
WORKDIR /app
ENV PYTHONUNBUFFERED=1
ENV PYTHONUNBUFFERED=1
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .