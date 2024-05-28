from os import path



# UPLOAD_PATH = os.path.join(server.root_path, "uploads")

class Config:
    
    PROJECT_ROOT = path.abspath(path.dirname(__file__))
    SECRET_KEY = "qwert123123123"
    # SQLACHEMY_DATABASE_RUI = "sqlite:///" + path.join(PROJECT_ROOT, "database.db")