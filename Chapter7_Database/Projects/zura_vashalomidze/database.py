from app import db
from model import Subject, Teacher, Student
import names


db.drop_all()
db.create_all()

# History teacher
teacher1 = Teacher("ana", "nikoleishvili")
#  Math teacher
teacher2 = Teacher("giorgi", "lemonjava")
db.session.add(teacher1)
db.session.add(teacher2)
db.session.commit()
# Subjects
subject1 = Subject("History", teacher1.id)
subject2 = Subject("Math", teacher2.id)
db.session.add(subject1)
db.session.add(subject2)
db.session.commit()

for i in range(4):
    student = Student(names.get_first_name(), names.get_last_name(), subject1.id)
    db.session.add(student)
    db.session.flush()
for i in range(4, 10):
    student = Student(names.get_first_name(), names.get_last_name(), subject2.id)
    db.session.add(student)
    db.session.flush()
db.session.commit()


