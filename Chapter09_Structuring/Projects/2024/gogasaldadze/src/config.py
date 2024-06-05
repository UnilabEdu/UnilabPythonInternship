from os import path

class Config:
    PROJECT_ROOT = path.abspath(path.dirname(__file__))
    SECRET_KEY = "mystrangesecretkey"
    SQLALCHEMY_DATABASE_URI = "sqlite:///" +  path.join(PROJECT_ROOT,"Databse.db")