from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


flask_app = Flask(__name__)
flask_app.config["SECRET_KEY"] = "sdjkafhjfhfwerhgiuweh"
flask_app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
flask_app.config["TRACK_DATABASE_MODIFICATIONS"] = False



UPLOAD_PATH = os.path.join(flask_app.root_path, 'static', 'uploads')




if __name__ == '__main__':
    from routes import *
    flask_app.run(debug=True)