from os import path


class Config(object):
    BASE_DIRECTORY = path.abspath(path.dirname(__file__))

    SECRET_KEY = "kljadskl10248120318znx"
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + path.join(BASE_DIRECTORY, "database.db")