from src import create_app
from src.extensions import db
from src.models import User, Post

db.create_all(app=create_app())
