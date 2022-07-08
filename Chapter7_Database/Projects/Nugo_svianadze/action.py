from models import Person, House
from app import db, app
from flask_migrate import Migrate

db.create_all()
migrate = Migrate(app, db)

persons = Person.query.all()
houses = House.query.all()

def add_person(name, age, house_id):
    person = Person(name, age, house_id)
    db.session.add(person)
    db.session.commit()
    return person


def add_house(address):
    house = House(address)
    db.session.add(house)
    db.session.commit()
    return house

random_persons = [
    ("Shane", 20, 1),
    ("Rick", 21, 3),
    ("Norman", 22, 1),
    ("Meggie", 23, 2),
    ("Sara", 24, 1),
    ("Lorie", 25, 3),
    ("Carl", 26, 1),]


def add_random_persons():
    for name, age, house_id in random_persons:
        add_person(name, age, house_id)

house = [
    "123 Main St",
    "456 gerogia St",
    "789 Walhala St",]

def add_random_houses():
    for address in house:
        print(address)
        add_house(address)

if not persons and not houses:
    add_random_persons()
    add_random_houses()
    for person in persons:
        print('Persons : ', person.name, person.age, person.house.address)
    for house in houses:
        print('Houses : ', house.address)

houses = House.query.all()
for house in houses:
    for person in house.people:
        print(house.address,person.name, person.age)