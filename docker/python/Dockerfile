# pull official base image
FROM python:3.8.3-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev \
    && apk add --virtual build-deps \
    && apk add jpeg-dev zlib-dev libjpeg \
    && pip install Pillow \
    && apk del build-deps

RUN pip install --upgrade pip

COPY ./requirements.txt .

RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./shell/entrypoint.sh .

# copy project
COPY . .

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/shell/entrypoint.sh"]