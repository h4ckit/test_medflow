FROM python:3.8.3-alpine

WORKDIR .
COPY . .

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev libc-dev libffi-dev libressl-dev

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT ["./entrypoint.sh"]