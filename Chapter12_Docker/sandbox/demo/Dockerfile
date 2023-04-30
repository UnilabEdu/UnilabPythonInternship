FROM python:3.11.1-slim-buster

WORKDIR /demo_project

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]