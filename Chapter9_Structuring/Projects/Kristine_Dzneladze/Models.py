from app import db 


class RegisterForm(db.Model):
    __tablename__ = "registerforms"

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String)
    lastname  = db.Column(db.String)
    email = db.Column(db.String)
    writer_experience = db.Column(db.String)
    writer_field = db.Column(db.String)
    essay_description = db.Column(db.String)
    uploaded_file = db.Column(db.String)


class Book(db.Model):
    __tablename__  = "books"

    id = db.Column(db.Integer, primary_key=True)
    bookname = db.Column(db.String)
    author  = db.Column(db.String)
    genre = db.Column(db.String)
    img_link = db.Column(db.String)
