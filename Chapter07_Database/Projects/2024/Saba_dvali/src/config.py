from os import path



# UPLOAD_PATH = os.path.join(server.root_path, "uploads")

class Config(object):
    
    PROJECT_ROOT = path.abspath(path.dirname(__file__))
    SECRET_KEY = "secret_key"
    # SQLACHEMY_DATABASE_RUI = "sqlite:///" + path.join(PROJECT_ROOT, "database.db")
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + path.join(PROJECT_ROOT, "database.db")



