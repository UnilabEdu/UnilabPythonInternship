from os import path
from datetime import timedelta

class Config(object):
    SECRET_KEY = "mysecretkey"
    BASE_DIR = path.abspath(path.dirname(__file__))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + path.join(BASE_DIR, 'db.sqlite')

    JWT_AUTH_URL_RULE = "/login"
    JWT_EXPIRATION_DELTA = timedelta(hours=1)