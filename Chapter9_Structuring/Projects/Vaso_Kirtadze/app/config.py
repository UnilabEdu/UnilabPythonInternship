import os

dirname = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = "VErygoodKEy"

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(dirname, 'db.sqlite')
SQLALCHEMY_TRACK_MODIFICATIONS = False