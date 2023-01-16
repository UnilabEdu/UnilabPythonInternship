from os import path




class Config(object):
    SECRET_KEY = "mysectretkey"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BASE_DIRECTORY = path.abspath(path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + path.join(BASE_DIRECTORY, 'db.sqlite')
