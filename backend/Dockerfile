FROM python:3.10-alpine

COPY . /app/backend

WORKDIR /app/backend

EXPOSE 8000

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt ./app/backend

RUN pip install -r /app/backend/requirements.txt

RUN adduser --disabled-password user

USER user
