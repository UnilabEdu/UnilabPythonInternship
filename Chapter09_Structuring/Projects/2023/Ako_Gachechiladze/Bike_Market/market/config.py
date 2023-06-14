from os import path


class Config(object):
    BASE_DIRECTORY = path.abspath(path.dirname(__file__))
    SECRET_KEY = "43ex5rtcgy hjkrctyg hj4sr6cytgh j"
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + path.join(BASE_DIRECTORY, "database.db")
   