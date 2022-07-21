from enum import unique
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisissecret'  # თუ დაგჭირდებათ და რამეში გამოგადეგაბთ აქ არის <3 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///University.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# ბაზას ვქმით ისე რა გამოვა :დ
class Student(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    full_name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    subject_id = db.relationship('Subject', backref ="subject", secondary = "active_student")
    faculty_id = db.relationship('Faculty', backref ="faculty", secondary = "active_student")

    def __repr__(self):
        return '<Student: {}>'.format(self.full_name)


class Subject(db.Model):
   
    id = db.Column(db.Integer, primary_key=True)
    subject_name = db.Column(db.String(50), unique = True)
    credits = db.Column(db.Integer)
    lecturer = db.Column(db.String(40))
    s_faculty_id = db.Column(db.Integer, db.ForeignKey('faculty.id'))

    def __repr__(self):
        return '<Subject: {}>'.format(self.subject_name)


class Faculty(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    faculty_name = db.Column(db.String(50), unique=True)
    max_student_amount = db.Column(db.Integer)
    dean  = db.Column(db.String(40), unique=True)
    faculty_students = db.relationship('ActiveStudent', backref ="student")
    faculty_subjects = db.relationship('Subject', backref ="subject")

    def __repr__(self):
        return '<Faculty: {}>'.format(self.faculty_name)



class ActiveStudent(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'))
    faculty_id = db.Column(db.Integer, db.ForeignKey('faculty.id'))




# db.drop_all()
# db.create_all()

# student1 = Student(public_id="qw2312341", full_name="zura begaddze", age = 18)
# student2 = Student(public_id="kfksdh34r", full_name="zura kjfk", age = 24)
# student3 = Student(public_id="sadasefsf", full_name="zubegaddze", age = 18 )
# student4 = Student(public_id="fasfeggds", full_name="zudgegaddze", age = 23)
# student5 = Student(public_id="sdgdgsdsd", full_name="zura", age = 18)

# subject1 = Subject(subject_name="jkasbbjas", credits=5, lecturer="sjabff sfdsg", s_faculty_id = 2)
# subject2 = Subject(subject_name="sfdfasvds", credits=3, lecturer="sdfngngrm gssdf", s_faculty_id = 2)
# subject3 = Subject(subject_name="ueutgfsbf", credits=5, lecturer="sjabff sfdsg", s_faculty_id = 3)
# subject4 = Subject(subject_name="fsdfguger", credits=10, lecturer="ejrk", s_faculty_id = 4)
# subjetc5 = Subject(subject_name="skdfknfks", credits=8, lecturer="sjadsgsdgs", s_faculty_id = 3)

# faculty1 = Faculty(faculty_name = "jbsajfbasn", max_student_amount=50, dean="aksbjs")
# faculty2 = Faculty(faculty_name = "jbsafasfss", max_student_amount=56, dean="werw")
# faculty3 = Faculty(faculty_name = "asffnenff,", max_student_amount=200, dean="wetet")
# faculty4 = Faculty(faculty_name = "lfmmdgirgr", max_student_amount=245, dean="wet")

# active1 = ActiveStudent(student_id=1, subject_id=2, faculty_id = 1)
# active2 = ActiveStudent(student_id=5, subject_id=2, faculty_id = 1)
# active3 = ActiveStudent(student_id=2, subject_id=3, faculty_id = 3)
# active4 = ActiveStudent(student_id=2, subject_id=5, faculty_id = 3)
# active5 = ActiveStudent(student_id=2, subject_id=5, faculty_id = 3)
# active6 = ActiveStudent(student_id=3, subject_id=1, faculty_id = 4)
# active7 = ActiveStudent(student_id=3, subject_id=1, faculty_id = 4)
# active8 = ActiveStudent(student_id=4, subject_id=4, faculty_id = 2)


# db.session.add_all([student1, student2, student3, student4, student5])
# db.session.add_all([subject1, subject2, subject3, subject4, subjetc5])
# db.session.add_all([faculty1, faculty2, faculty3, faculty4])
# db.session.add_all([active1, active2, active3, active4, active5, active6, active7, active8])

# db.session.commit()
