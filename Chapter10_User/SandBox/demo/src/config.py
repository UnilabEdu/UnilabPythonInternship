from os import path


class Config(object):
    BASE_DIRECTORY = path.abspath(path.dirname(__file__))
    UPLOAD_DIRECTORY = path.join(BASE_DIRECTORY, "static")
    FLASK_ADMIN_SWATCH = "cosmo"

    SECRET_KEY = "kljadskl10248120318znx"
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + path.join(BASE_DIRECTORY, "database.db")