import os

SECRET_KEY = "secretkey"
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(basedir, "data1.sqlite")}'
SQLALCHEMY_TRACK_MODIFICATIONS = False