from app import db
from modules import Student, Course, StudentCourse

# db.create_all()

john = Student('John', 'Brown', 18, 'johnbrown@gmail.com')
alice = Student('Alice', 'Sunderland', 19, 'alicesunderland@gmail.com')
bobby = Student('Bobby', 'Smith', 20, 'bobbysmith@gmail.com')

programming = Course('Programming',)
cyber_security = Course('Cyber Security',)

db.session.add_all([john, alice, bobby])
db.session.add_all([programming, cyber_security])
db.session.flush()

student_course_1 = StudentCourse(john.id, programming.id)
student_course_2 = StudentCourse(john.id, cyber_security.id)
student_course_3 = StudentCourse(alice.id, programming.id)
student_course_4 = StudentCourse(bobby.id, cyber_security.id)

db.session.add_all([student_course_1, student_course_2, student_course_3, student_course_4])
db.session.commit()
