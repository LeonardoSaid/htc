FROM python:3.9-alpine

ENV PYTHONPATH /app/src

WORKDIR /app
COPY Pipfile ./

RUN apk add build-base linux-headers

RUN pip install --upgrade pip \
    && python -m pip install --upgrade setuptools \
    && pip install pipenv \
    && pipenv install --dev

COPY . .

CMD pipenv run python ./src/main.py