from src.extensions import db

# ONE - TO - MANY Relationship
class University(db.Model):

    __tablename__ = "universities"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    location = db.Column(db.String)
    students = db.relationship("Student", back_populates="university")

    def __repr__(self):
        return f"{self.name}"


class Student(db.Model):
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    surname = db.Column(db.String)
    faculty = db.Column(db.String)

    university_id = db.Column(db.ForeignKey("universities.id"))
    university = db.relationship("University", back_populates="students")

    def __repr__(self):
        return f"{self.name} {self.surname}"