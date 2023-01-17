from os import path, sep, pardir



class Config(object):
    SECRET_KEY = "Vassalis"
    BASE_DIR = path.abspath(path.dirname(__file__) + sep + pardir)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + path.join(BASE_DIR, 'db.sqlite')