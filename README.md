# Simple helloworld app

## Dockerfile:

```sh
FROM alpine

MAINTAINER vladskvortsov

COPY app.py /opt/

COPY templates /opt/templates/

RUN apk --update add python3 py-pip && pip install flask --upgrade

ENTRYPOINT FLASK_APP=/opt/app.py flask run --host 0.0.0.0 --port 5000

```

To run the app, first build docker image:

```sh
docker build . -t alpine-flask
```

And run with setting a port:

```sh
docker run -d -p 5000:5000 alpine-flask
```

Now make sure all working accesing:

```sh
localhost:5000
```
