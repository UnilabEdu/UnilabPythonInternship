from db import db


class BaseModel(db.Model):
    __abstract__ = True

    def save(self):
        db.session.commit()

    def create(self, commit=True):
        db.session.add(self)

        if commit:
            self.save()
        else:
            db.session.flush()

    def delete(self):
        db.session.delete(self)
        self.save()


class Human(BaseModel):
    __tablename__ = "people"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    birth_year = db.Column(db.String)

    def __repr__(self):
        return f"{self.first_name} {self.last_name} (Human)"


class User(BaseModel):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    email_address = db.Column(db.String)
    phone_number = db.Column(db.String)
    password = db.Column(db.String)
    human_id = db.Column(db.Integer, db.ForeignKey("people.id"))

    human = db.relationship("Human", uselist=False)

    def __repr__(self):
        return f"{self.username} (User)"


class Book(BaseModel):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    publication_year = db.Column(db.String)

    authors = db.relationship("Author", secondary="authors_books", back_populates="books")
    categories = db.relationship("Category", secondary="categories_books", back_populates="books")
    publishers = db.relationship("Publisher", secondary="publishers_books", back_populates="books")

    def __repr__(self):
        return f"{self.title} (Book)"


class Author(BaseModel):
    __tablename__ = "authors"

    id = db.Column(db.Integer, primary_key=True)
    human_id = db.Column(db.Integer, db.ForeignKey("people.id"))

    human = db.relationship("Human", uselist=False)

    books = db.relationship("Book", secondary="authors_books", back_populates="authors")

    def __repr__(self):
        return f"{' '.join(self.human.__repr__().split()[:-1])} (Author)"


class Category(BaseModel):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    books = db.relationship("Book", secondary="categories_books", back_populates="categories")

    def __repr__(self):
        return f"{self.name} (Category)"


class Publisher(BaseModel):
    __tablename__ = "publishers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    books = db.relationship("Book", secondary="publishers_books", back_populates="publishers")

    def __repr__(self):
        return f"{self.name} (Publisher)"


# Many-to-many relationship tables
class AuthorBook(BaseModel):
    __tablename__ = 'authors_books'

    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey("authors.id"))
    book_id = db.Column(db.Integer, db.ForeignKey("books.id"))


class PublisherBook(BaseModel):
    __tablename__ = "publishers_books"

    id = db.Column(db.Integer, primary_key=True)
    publisher_id = db.Column(db.Integer, db.ForeignKey("publishers.id"))
    book_id = db.Column(db.Integer, db.ForeignKey("books.id"))


class CategoryBook(BaseModel):
    __tablename__ = "categories_books"

    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"))
    book_id = db.Column(db.Integer, db.ForeignKey("books.id"))
