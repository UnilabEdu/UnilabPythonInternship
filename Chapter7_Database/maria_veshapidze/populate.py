from myapp import db, Tutor, Student

db.create_all()

tutor1 = Tutor('Maria', 'Maths')
db.session.add(tutor1)
db.session.commit()

student1 = Student('Ia', 'Algebra 1', tutor1.id)
db.session.add(student1)
db.session.commit()

maria = Tutor.query.filter_by(name='Maria').first()
print(maria)
