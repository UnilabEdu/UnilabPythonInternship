FROM python:3.11.3-slim-buster

WORKDIR /demo

COPY . .

RUN pip install --upgrade pip
RUN apt-get update && apt-get -y install python3-dev gcc build-essential
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["uwsgi", "uwsgi.ini"]