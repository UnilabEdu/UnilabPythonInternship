import os
import json

from pathlib import Path

from app.extensions import login_manager


BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR_APP = Path(__file__).resolve().parent

# Don't forget to add config.json to .gitignore in the production
with open(os.path.join(BASE_DIR, 'config.json')) as config_file:
    config = json.load(config_file)

SECRET_KEY = config["SECRET_KEY"]
SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://dbuser:dbpass@localhost:5432/db_name'
SQLALCHEMY_TRACK_MODIFICATIONS = False

login_manager.login_view = "login"
