from src.extensions import db
from src.models import BaseModel


class Publisher(BaseModel):
    __tablename__ = "publishers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    books = db.relationship("Book", secondary="publishers_books", back_populates="publishers")

    def __repr__(self):
        return f"{self.name} (Publisher)"


class PublisherBook(BaseModel):
    __tablename__ = "publishers_books"

    id = db.Column(db.Integer, primary_key=True)
    publisher_id = db.Column(db.Integer, db.ForeignKey("publishers.id"))
    book_id = db.Column(db.Integer, db.ForeignKey("books.id"))
