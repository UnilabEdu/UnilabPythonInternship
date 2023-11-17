from app import flask_app
from db import db
from models import Product


with flask_app.app_context():
    db.create_all()