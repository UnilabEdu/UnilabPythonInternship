import os


class Config(object):

    PROJECT = "Demo App"
    PROJECT_NAME = "Demo App"
    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    SECRET_KEY = "sup3rs3kr3tk3y"
    DEBUG = True

    # Flask-SQLAlchemy
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + PROJECT_ROOT + '/db.sqlite'

    # Flask-User
    USER_APP_NAME = "Demo App"
    USER_ENABLE_EMAIL = False
    USER_ENABLE_USERNAME = True
    USER_LOGIN_URL = "/login"
    USER_LOGOUT_URL = "/logout"
    USER_REGISTER_URL = "/register"