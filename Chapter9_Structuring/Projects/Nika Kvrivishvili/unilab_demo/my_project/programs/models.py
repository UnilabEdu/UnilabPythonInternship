from my_project import db


class Program(db.Model):
    __tablename__ = 'programs'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    students = db.relationship('Student', backref='student')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

    @classmethod
    def get_choices(cls):
        program_data = Program.query.all()
        choices = []
        for program in program_data:
            choices.append((program.id, program.name))

        return choices

    def add(self):
        db.session.add(self)
        db.session.commit()
