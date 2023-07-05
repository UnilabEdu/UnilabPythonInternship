from os import path


class Config(object):
    BASE_DIRECTORY = path.abspath(path.dirname(__file__))
    UPLOAD_PATH = path.join(BASE_DIRECTORY, "uploads")

    SECRET_KEY = "kljadskl10248120318znx"
    SERIALIZER_SALT = "fakldajkls14"
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + path.join(BASE_DIRECTORY, "database.db")

    # Flask-Mail
    MAIL_SERVER = "sandbox.smtp.mailtrap.io"
    MAIL_PORT = 2525
    MAIL_USERNAME = "ENTER_YOUR_USERNAME"
    MAIL_PASSWORD = "ENTER_YOUR_PASSWORD"
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_DEBUG = False

    BABEL_TRANSLATION_DIRECTORIES = "../translations"


class TestConfig(object):
    BASE_DIRECTORY = path.abspath(path.dirname(__file__))
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + path.join(BASE_DIRECTORY, "tests.db")
    WTF_CSRF_ENABLED = False
