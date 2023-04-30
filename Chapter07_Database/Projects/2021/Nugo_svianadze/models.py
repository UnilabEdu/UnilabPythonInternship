from app import db

class Person(db.Model):
    __tablename__ = "person"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    birth_place = db.Column(db.String(50), nullable=False, default="Unknown")
    house_id = db.Column(db.Integer, db.ForeignKey("house.id"))

    def __init__(self, name, age, house_id):
        self.name = name
        self.age = age
        self.house_id = house_id


class House(db.Model):
    __tablename__ = "house"
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(50), nullable=False)
    people = db.relationship("Person", backref="house", lazy=True)

    def __init__(self, address):
        self.address = address




