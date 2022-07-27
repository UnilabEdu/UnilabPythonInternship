import os

SECRET_KEY = 'random_key'
projectdir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(projectdir, 'database.sqlite')
SQLALCHEMY_TRACK_MODIFICATIONS = False
CSRF_ENABLED = True
