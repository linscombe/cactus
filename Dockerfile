# syntax=docker/dockerfile:1
FROM python:3.10.1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# RUN apt-get update && apt-get install -y \
#   xmlsec1 \
#   && rm -rf /var/lib/apt/lists/*

WORKDIR /code
COPY . /code/

RUN pip install Django==3.2.10
RUN pip install PyGithub

