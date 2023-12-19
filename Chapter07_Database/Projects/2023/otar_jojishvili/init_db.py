from db import db
from models import Users
from app import app


with app.app_context():
    db.create_all()