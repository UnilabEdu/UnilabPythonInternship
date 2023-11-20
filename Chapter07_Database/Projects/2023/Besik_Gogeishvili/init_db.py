from app import app
from db import db
from models import Petition

with app.app_context():
    db.create_all()