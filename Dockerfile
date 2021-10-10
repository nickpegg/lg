FROM python:3.9-slim

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

ENV HTTP_PORT 8000
ENV NUM_WORKERS 4

ENV FLASK_APP glass.py

EXPOSE ${HTTP_PORT}

WORKDIR /app

RUN	apt-get update
RUN	apt-get install -y mtr-tiny iputils-ping

RUN pip install --no-cache-dir poetry
COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

COPY . .

RUN	/app/extra/adduser.sh

USER lg
CMD gunicorn -w ${NUM_WORKERS} -b 0.0.0.0:${HTTP_PORT} --capture-output --access-logfile - --log-file - glass:app
