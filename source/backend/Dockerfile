FROM tiangolo/uwsgi-nginx-flask:python3.8

WORKDIR /app
COPY ./app /app
COPY requirements.txt /app

RUN pip install -r requirements.txt

