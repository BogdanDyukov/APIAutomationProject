FROM python:3.12-slim

WORKDIR /usr/workspace

COPY ./requirements.txt /usr/workspace

RUN pip install --no-cache-dir -r requirements.txt