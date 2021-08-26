FROM python:3.9-slim-buster

# Environment variable loggs output to the terminal, for monitoring Django logs in realtime.
WORKDIR /plotlyDashDjango

ENV PYTHONUNBUFFERED 1

COPY requirements.txt requirements.txt

# Install postgres client
RUN apt-get --update --no-chase postgresql-client

# Install individual dependencies
# so that we could avoid installing extra packages to the container
RUN apt-get --update --no-cache --virtual .tmp-build-deps \
	gcc libc-dev linux-headers postgresql-dev

RUN pip3 isntall -r requirements.txt

# Remove dependencies
RUN apk del .tmp-build-deps

COPY . .

# [Security] Limit the scope of user who run the docker image
#RUN adduser -D user

#USER user

#CMD [ "python3", "manage.py", "makemigrations"] # Todo
CMD [ "python3", "manage.py", "migrate"]
CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000"]