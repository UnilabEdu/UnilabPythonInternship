from app import db

class Coach(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(24))
    age = db.Column(db.Integer)
    pupils = db.relationship('Pupil', backref='coach')

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Pupil(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(24))
    is_active = db.Column(db.Boolean, default=True)
    coach_id = db.Column(db.Integer, db.ForeignKey('coach.id'))

    def __init__(self, name, is_active, coach_id):
        self.name = name
        self.is_active = is_active
        self.coach_id = coach_id



class Fighter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(24))

    organizations = db.relationship('Organization', secondary='connector')

    def __init__(self, name):
        self.name = name


class Organization(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(24))

    def __init__(self, name):
        self.name = name


class Connector(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fighter_id = db.Column(db.Integer, db.ForeignKey('fighter.id'))
    organization_id = db.Column(db.Integer, db.ForeignKey('organization.id'))

    def __init__(self, figter_id, org_id):
        self.fighter_id = figter_id
        self.organization_id = org_id






