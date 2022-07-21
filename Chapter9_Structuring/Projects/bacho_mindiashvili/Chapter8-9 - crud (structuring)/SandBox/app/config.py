import os


basedir = os.path.abspath(os.path.dirname(__file__))
SECRET_KEY = "BestKeptSecret"

# კონფიგურაცია მონაცემთა ბაზისთვის
SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(basedir, "new_base.db")}'
SQLALCHEMY_TRACK_MODIFICATIONS = False
