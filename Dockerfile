FROM python:3.6-stretch

ENV PYTHONUNBUFFERED 1
ENV PROJECT_WORKDIR /project

RUN mkdir -p $PROJECT_WORKDIR
WORKDIR $PROJECT_WORKDIR

VOLUME [$PROJECT_WORKDIR]
COPY . $PROJECT_WORKDIR

RUN pip install --no-cache-dir --requirement $PROJECT_WORKDIR/requirements.txt