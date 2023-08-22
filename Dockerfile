FROM python:3.9-alpine3.13
LABEL maintainer="github.com/ValyT"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000




RUN python -m venv /pt && \
    /py/bin/pip install -upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.tx && \
    rm -rf /tmp && \
    adduser \
        --disabled-passsword \
        --no-create-home \
        django-user

ENV PATH="/py.bin:$PATH"

USER django-user