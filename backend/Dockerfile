FROM python:3.10-alpine

COPY . /app

WORKDIR /app

EXPOSE 8000

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN adduser --disabled-password user

USER user
