FROM python:3
MAINTAINER Kouts Vladimir <kvn12@ukr.net>

ENV TERM=xterm
RUN apt-get update && pip install Flask xlwt xlrd lxml flask-migrate flask-sqlalchemy flask-admin

EXPOSE 8000