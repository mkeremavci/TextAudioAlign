FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt .

RUN apt-get update
RUN apt-get install libgomp1 ffmpeg libsm6 libxext6 -y

RUN pip install -r requirements.txt

COPY ./api ./api

EXPOSE 3100

CMD uvicorn api.manage:app --reload --host 0.0.0.0 --port 3100