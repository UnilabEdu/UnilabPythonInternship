from manager import db, NursesModel

nurse = NursesModel('tskaro@gmail.com', 'Giorgi', 'Tskaroveli', 'Khresili 24', 'Cardiology', 16)
print(nurse.id)

db.session.add(nurse)
db.session.commit()

print(nurse.id)