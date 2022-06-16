FROM python:3.10

WORKDIR /opt/app
EXPOSE 8000

COPY run_uwsgi.sh requirements.txt uwsgi.ini ./

RUN  mkdir -p /var/www/static/ \
     && mkdir -p /var/www/media/ \
     && mkdir -p /opt/app/static/ \
     && mkdir -p /opt/app/media/ \
     && apt-get update -y \
     && pip install --upgrade pip \
     && pip install -r requirements.txt

COPY . .

ENTRYPOINT ["uwsgi", "--strict", "--ini", "uwsgi.ini"]
