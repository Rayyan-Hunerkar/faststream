# syntax=docker/dockerfile:1


FROM python:3.10-alpine3.16

WORKDIR /faststream
COPY requirements.txt /faststream/
RUN apk update
RUN apk add gcc python3-dev musl-dev libffi-dev
RUN pip install -r requirements.txt
COPY . /faststream/
