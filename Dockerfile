FROM python:3.6-alpine

ENV PYTHONUNBUFFERED 1
RUN mkdir /config
ADD config/requirements.txt /config/

RUN set -ex \
    && apk add --no-cache --virtual .build-deps \
            gcc \
            make \
            libc-dev \
            musl-dev \
            linux-headers \
    && apk add --no-cache --virtual .crypto-rundeps \
	--repository http://dl-cdn.alpinelinux.org/alpine/edge/main \
	libressl2.7-libcrypto \ 
    && pip install -U pip \
    && LIBRARY_PATH=/lib:/usr/lib /bin/sh -c "pip install --no-cache-dir -r /config/requirements.txt"

RUN mkdir /src
COPY src /src 

WORKDIR /src

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]