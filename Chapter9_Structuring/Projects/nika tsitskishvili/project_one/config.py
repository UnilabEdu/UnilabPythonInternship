import os
class TConfig(object):
    SECRET_KEY = "wekjffghj"
    project_dir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(project_dir, 'db3.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False



