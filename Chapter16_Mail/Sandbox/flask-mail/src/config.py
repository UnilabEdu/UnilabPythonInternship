from os import path

class Config(object):
    SECRET_KEY = "mysecretkey"
    BASE_DIR = path.abspath(path.dirname(__file__))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + path.join(BASE_DIR, 'db.sqlite')