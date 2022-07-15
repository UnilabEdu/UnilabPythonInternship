from app import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return f"Student: {self.first_name}"
