# pull official base image
FROM python:3.10.1-slim-buster

# set work directory
WORKDIR /usr/backend/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get -y install pipenv \
    && pip install --upgrade pip setuptools wheel \
    && apt-get clean

# install dependencies
COPY ./Pipfile .
COPY ./Pipfile.lock .
RUN pipenv install --system --deploy


# copy project
COPY . /usr/backend/app/
