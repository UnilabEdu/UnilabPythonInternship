from app import db
class SubjectModel(db.Model):
    __tablename__ = 'subject'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    students = db.Column(db.String, nullable=False)
    teacher = db.Column(db.String, nullable=False) #შეამოწმე

    def __repr__(self):
        return f"Subject {self.title}"
class TeacherModel(db.Model):
    __tablename__ = "Teachers"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    subject_id = db.Column(db.String(20), db.ForeignKey('subject.id'), nullable=False)

    def __repr__(self):
        return f"Teacher {self.first_name+' '+self.last_name}"

class StudentModel(db.Model):
    __tablename__ = "Students"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    subject_id = db.Column(db.String(20), db.ForeignKey('subject.id'), nullable=False)

    def __repr__(self):
        return f"Student {self.first_name+' '+self.last_name}"

