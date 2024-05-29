from os import path


class Config:
    BASE_DIRECTORY = path.abspath(path.dirname(__file__))
    UPLOAD_PATH = path.join(BASE_DIRECTORY, 'static', 'uploads')
    SECRET_KEY = "sdjkafhjfhfwerhgiuweh"
    SQLALCHEMy_DATABASE_URI = "sqlite:///" + path.join(BASE_DIRECTORY, "database.db")


