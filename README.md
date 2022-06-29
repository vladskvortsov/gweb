Simple hello file

Dockerfile:

FROM alpine

MAINTAINER vlad <vladskvortsov96@gmail.com>

COPY hello.py /opt/app.py

RUN apk update

RUN apk add python3

RUN apk add py-pip

RUN apk add sudo

RUN sudo pip install flask --upgrade

ENTRYPOINT FLASK_APP=/opt/app.py flask run --host 0.0.0.0
