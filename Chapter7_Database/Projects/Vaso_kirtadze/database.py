from app import db
from model import Coach, Pupil, Fighter, Organization, Connector

db.drop_all()
db.create_all()

coach1 = Coach("MIke Brown", 46)
coach2 = Coach("Trevor Wittman", 48)


db.session.add_all([coach1, coach2])
db.session.flush()

pupil1 = Pupil("Dustin Poirier", True, 1)
pupil2 = Pupil("Jorge Masvidal", True, 1)
pupil3 = Pupil("Joanna Jedrzejczyk", False, 1)
pupil4 = Pupil("Kamaru Usman", True, 2)
pupil5 = Pupil("Rose Namajunas", True, 2)

db.session.add_all([pupil1, pupil2, pupil3, pupil4, pupil5])
db.session.commit()


pupils = Pupil.query.filter_by(coach_id=1).all()
for pupil in pupils:
    print(pupil.name)

coach = Coach.query.get(1)
print(coach.pupils)

pupil = Pupil.query.get(5)
print(pupil.coach.name)
print("*********")

organization1 = Organization("UFC")
organization2 = Organization("BELLATOR")
organization3 = Organization("ONE FC")
db.session.add_all([organization1, organization2, organization3])
db.session.flush()


fighter1 = Fighter("Michael Chandler") #Has fought in UFC and BELLATOR
fighter2 = Fighter("Eddie Alvarez")   #Has fought in all 3 organizations
fighter3 = Fighter("Max Holloway")       #Has fought in UFC only

db.session.add_all([fighter1, fighter2, fighter3])
db.session.flush()

connector1 = Connector(fighter1.id, organization1.id)
connector2 = Connector(fighter1.id, organization2.id)

connector4 = Connector(fighter2.id, organization1.id)
connector5 = Connector(fighter2.id, organization2.id)
connector6 = Connector(fighter2.id, organization3.id)

connector7 = Connector(fighter3.id, organization1.id)

db.session.add_all([connector1, connector2, connector4, connector5, connector6, connector7])
db.session.commit()

fighter1 = Fighter.query.get(2)
for item in fighter1.organizations:
    print(item.name)