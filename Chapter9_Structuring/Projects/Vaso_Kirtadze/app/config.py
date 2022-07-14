import os


class test_config:
    SECRET_KEY = "VErygoodKEy"

    dirname = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(dirname, 'data.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False