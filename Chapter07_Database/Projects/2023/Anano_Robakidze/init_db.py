from db import db
from app import app
from models import Product

with app.app_context():
    db.create_all()