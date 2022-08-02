import os

class Config():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_name = 'data.sqlite'

    SECRET_KEY = 'my_secret_key'

    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(base_dir, db_name)}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False