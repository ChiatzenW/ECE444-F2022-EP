# syntax=docker/dockerfile:1

FROM python:3.10-slim

COPY . .
RUN pip3 install -r requirements.txt

ENV FLASK_ENV development
WORKDIR Education_Pathways

CMD ["flask", "--app", "index", "--debug", "run"]