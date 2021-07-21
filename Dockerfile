FROM python:3.8.6-alpine3.12 as base

RUN apk --no-cache add --virtual build-dependencies libffi-dev openssl-dev build-base gcc libxml2-dev libxslt-dev

COPY requirements.txt /usr/local/dc/collector-requirements.txt
RUN pip install  -r /usr/local/dc/collector-requirements.txt

COPY zetra     /usr/local/dc/zetra
COPY collector /usr/local/dc/collector

ENV PYTHONPATH /usr/local/dc

COPY .pylintrc /etc/pylintrc
RUN python -mpylint --unsafe-load-any-extension=y collector
RUN python -mpylint --unsafe-load-any-extension=y zetra

ENTRYPOINT ["python", "-m", "collector"]