FROM python:3.8.13-slim-bullseye

WORKDIR /usr/src/app

# Copy all the files into the container
COPY . .

ENV FLASK_APP=app \
    FLASK_ENV=production

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
