FROM python:3.11-slim
RUN apt update -y
RUN apt install build-essential -y
RUN apt install apache2 libapache2-mod-wsgi-py3 -y
RUN apt-get update
RUN apt-get install -y --no-install-recommends postgresql-client
RUN rm -rf /var/lib/apt/lists/*
RUN mkdir -p /django/site/public/media /django/site/public/static /django/site/logs
COPY ./cs415/ /django/
WORKDIR /django/
RUN python3 -m venv /django/env
RUN /django/env/bin/pip3 install -r requirements.txt
RUN /django/env/bin/python manage.py collectstatic

COPY ./000-default.conf /etc/apache2/sites-available/

CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]

EXPOSE 80