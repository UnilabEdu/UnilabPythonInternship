FROM python:3.11.1-slim-buster

WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN apt-get update && apt-get -y install python3-dev gcc build-essential
RUN pip install -r requirements.txt

RUN chmod +x /app/flask_app.sh

EXPOSE 5000

RUN /app/flask_app.sh

CMD ["uwsgi", "uwsgi.ini"]