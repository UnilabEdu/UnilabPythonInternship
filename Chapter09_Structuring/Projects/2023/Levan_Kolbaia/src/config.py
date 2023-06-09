from os import path

class Config(object):
    BASE_DIRECTORY = path.abspath(path.dirname(__file__))

    SECRET_KEY="NL"
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + path.join(BASE_DIRECTORY, "src/database.db")



