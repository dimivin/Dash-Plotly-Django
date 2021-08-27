FROM postgres:latest

RUN apt update
RUN apt -y upgrade


# install Python 3
RUN apt-get update && apt-get install -y python3 python3-pip

RUN apt-get install libpq-dev
RUN apt-get install postgresql

RUN apt-get install gcc
RUN apt-get install python3-dev

#RUN apt-get install musl-dev1.1.24 Todo this was not installed

COPY . .

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

# install psycopg2 library with PIP
#RUN pip3 install psycopg2

# install the Django library
#RUN pip3 install Django

# add the 'postgres' admin role
USER postgres

# expose Postgres port
EXPOSE 5432

# expose port for Django
EXPOSE 8000

#FROM python:3.9-slim-buster
#
## Environment variable loggs output to the terminal, for monitoring Django logs in realtime.
#WORKDIR /plotlyDashDjango
#
#ENV PYTHONUNBUFFERED 1
#
#COPY requirements.txt requirements.txt
#
## Install postgres client
#RUN apt-get --update --no-chase postgresql-client
#
## Install individual dependencies
## so that we could avoid installing extra packages to the container
#RUN apt-get --update --no-cache --virtual .tmp-build-deps \
#	gcc libc-dev linux-headers postgresql-dev
#
#RUN pip3 isntall -r requirements.txt
#
## Remove dependencies
#RUN apk del .tmp-build-deps
#
#COPY . .
#
## [Security] Limit the scope of user who run the docker image
##RUN adduser -D user
#
##USER user
#
##CMD [ "python3", "manage.py", "makemigrations"] # Todo
#CMD [ "python3", "manage.py", "migrate"]
#CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000"]