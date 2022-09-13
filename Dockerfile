FROM python:slim-buster

ENV PYTHONBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

