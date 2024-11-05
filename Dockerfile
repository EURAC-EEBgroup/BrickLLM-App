FROM python:3.12

WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHON UNBUFFERED 1
ENV DOCKER_RUNNING True
ENV REDIS_URL_BROKER 'redis://redis:6379/0'
ENV REDIS_URL_BACKEND 'redis://redis:6379/1'

RUN apt-get update && apt-get install -y \
    build-essential

COPY ./requirements.txt /app/requirements.txt
# COPY ./dist_brick_local /app/dist_brick_local
RUN pip3 install --no-cache-dir --upgrade -r /app/requirements.txt

# COPY ./Pipfile .
# RUN pip3 install pipenv
# RUN pipenv install --skip-lock 

COPY ./BrickApp /app
