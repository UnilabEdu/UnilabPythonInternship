from os import path


class Config(object):
    BASE_DIRECTORY = path.abspath(path.dirname(__file__))
    UPLOAD_PATH = path.join(BASE_DIRECTORY, "uploads")
    FLASK_ADMIN_SWATCH = "superhero"

    SECRET_KEY = "kljadskl10248120318znx"
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + path.join(BASE_DIRECTORY, "database.db")