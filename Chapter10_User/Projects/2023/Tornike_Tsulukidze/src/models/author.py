from src.extensions import db
from src.models import BaseModel


class Author(BaseModel):
    __tablename__ = "authors"

    id = db.Column(db.Integer, primary_key=True)
    human_id = db.Column(db.Integer, db.ForeignKey("people.id"))

    human = db.relationship("Human", uselist=False)

    books = db.relationship("Book", secondary="authors_books", back_populates="authors")

    def __repr__(self):
        return f"{' '.join(self.human.__repr__().split()[:-1])} (Author)"


class AuthorBook(BaseModel):
    __tablename__ = 'authors_books'

    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey("authors.id"))
    book_id = db.Column(db.Integer, db.ForeignKey("books.id"))
