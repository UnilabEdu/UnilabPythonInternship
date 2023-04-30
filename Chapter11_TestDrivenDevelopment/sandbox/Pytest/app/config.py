import os


class Config(object):

    PROJECT = "MovieLab"
    PROJECT_NAME = "MovieLab"
    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    SECRET_KEY = "D0N75H4r3W17H4NY0N3"
    DEBUG = True

    # Flask-SQLAlchemy
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + PROJECT_ROOT + '/db.sqlite'
