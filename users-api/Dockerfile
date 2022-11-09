FROM python:3.10-slim-bullseye

ADD ./users-api/src /app
ADD ./users-api/data/users.json /app/users.json

RUN pip install -r /app/requirements.txt

WORKDIR /app

CMD ["./docker-entrypoint.sh"]

