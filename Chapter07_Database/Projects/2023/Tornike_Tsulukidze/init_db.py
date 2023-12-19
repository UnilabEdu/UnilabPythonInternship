from app import app
from db import db
from models import User, Book, Author, Publisher, Category, AuthorBook, PublisherBook, CategoryBook, Human


with app.app_context():
    db.create_all()
