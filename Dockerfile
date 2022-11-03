FROM alpine

MAINTAINER vladskvortsov

COPY app.py /opt/

COPY templates /opt/templates/

RUN apk --update add python3 py-pip && pip install flask --upgrade

ENTRYPOINT FLASK_APP=/opt/app.py flask run --host 0.0.0.0 --port 5000
