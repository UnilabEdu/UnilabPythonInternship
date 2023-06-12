from flask_sqlalchemy import SQLAlchemy
from flask-migrate import Migrate

db = SQLAlchemy()

migrate = Migrate()