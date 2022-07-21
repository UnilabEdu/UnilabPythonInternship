from app import db


class Type(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(24))
    users = db.relationship('User', backref='type')

    def __init__(self, name):
        self.name = name


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(24))
    email = db.Column(db.String(48))
    password = db.Column(db.String(48))
    experience = db.Column(db.String(24))
    type_id = db.Column(db.Integer, db.ForeignKey('type.id'))

    def __init__(self, username, email, password, experience, type_id):
        self.username = username
        self.email = email
        self.password = password
        self.experience = experience
        self.type_id = type_id

