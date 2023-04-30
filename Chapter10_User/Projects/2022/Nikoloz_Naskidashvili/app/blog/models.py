from app.extensions import db
from app.models.models import BaseModel


class Article(db.Model, BaseModel):
	__tablename__ = "blog_article"

	title = db.Column(db.String, nullable=False)
	body = db.Column(db.Text, nullable=False)
	date = db.Column(db.Date, nullable=False)
	preview_img = db.Column(db.String)
