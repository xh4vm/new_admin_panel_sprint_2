FROM python:3.10

WORKDIR /opt/app
EXPOSE 8000
ENTRYPOINT ["uwsgi", "--strict", "--ini", "uwsgi.ini"]

COPY run_uwsgi.sh requirements.txt uwsgi.ini ./

RUN  mkdir -p /var/www/static/ \
     && pip install --upgrade pip \
     && pip install -r requirements.txt

COPY . .
