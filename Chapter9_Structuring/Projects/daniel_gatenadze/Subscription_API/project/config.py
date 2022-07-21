import os


class ConfigMain(object):
    projectdir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(projectdir, '../../db.sqlite')
    SECRET_KEY = "Secret_Password"
