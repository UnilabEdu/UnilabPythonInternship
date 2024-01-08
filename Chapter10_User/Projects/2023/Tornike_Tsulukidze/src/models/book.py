from src.extensions import db
from src.models import BaseModel


class Book(BaseModel):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    publication_year = db.Column(db.String)

    authors = db.relationship("Author", secondary="authors_books", back_populates="books")
    categories = db.relationship("Category", secondary="categories_books", back_populates="books")
    publishers = db.relationship("Publisher", secondary="publishers_books", back_populates="books")

    def __init__(self, title, publication_year):
        self.title = title
        self.publication_year = publication_year

    def __repr__(self):
        return f"{self.title} (Book)"


class Category(BaseModel):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    books = db.relationship("Book", secondary="categories_books", back_populates="categories")

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"{self.name} (Category)"


class CategoryBook(BaseModel):
    __tablename__ = "categories_books"

    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"))
    book_id = db.Column(db.Integer, db.ForeignKey("books.id"))

    def __init__(self, category_id, book_id):
        self.category_id = category_id
        self.book_id = book_id
