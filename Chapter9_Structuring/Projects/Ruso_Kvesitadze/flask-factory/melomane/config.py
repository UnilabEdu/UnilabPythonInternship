from os import path

class Config(object):
    SECRET_KEY = "mysecretkey"
    base_directory = path.abspath(path.dirname(__file__))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + path.join(base_directory, "db.sqlite")



