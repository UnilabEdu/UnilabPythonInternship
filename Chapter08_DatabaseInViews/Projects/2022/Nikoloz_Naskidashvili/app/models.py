from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from app import app

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Article(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String, nullable=False)
	body = db.Column(db.Text, nullable=False)
	date = db.Column(db.Date, nullable=False)
	preview_img = db.Column(db.String)
