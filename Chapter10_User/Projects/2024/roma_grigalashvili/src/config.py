from os import path, environ


class Config(object):
    BASE_DIRECTORY = path.abspath(path.dirname(__file__))

    SECRET_KEY = "kljadskl10248120318znx"

    if environ.get("FLASK_DB") == "development":
        SQLALCHEMY_DATABASE_URI = "sqlite:///" + path.join(BASE_DIRECTORY, "database.db")
    elif environ.get("FLASK_DB") == "production":
        SQLALCHEMY_DATABASE_URI = "sqlite:///" + path.join(BASE_DIRECTORY, "database.sqlite")
    else :
        SQLALCHEMY_DATABASE_URI = "sqlite:///" + path.join(BASE_DIRECTORY, "db.sqlite")