from my_project import db


class Student(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    program_id = db.Column(db.Integer, db.ForeignKey("programs.id"))

    def __init__(self, name, email, program_id):
        self.name = name
        self.email = email
        self.program_id = program_id

    def __repr__(self):
        return self.name

    @classmethod
    def get_by_id(cls, _id):
        user_by_id = Student.query.get(_id)
        return user_by_id

    def create(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
