import os
from .extensions import login_manager


class ConfigMain(object):
    projectdir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(projectdir, '../../db.sqlite')
    SECRET_KEY = "Secret_Password"
    login_manager.login_view = "auth.log_in"
