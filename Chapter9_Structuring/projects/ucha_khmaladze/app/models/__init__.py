from app import db


class Reservation(db.Model):
    __tablename__ = 'reservations'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    last_name = db.Column(db.String)
    date_from = db.Column(db.Date)
    date_to = db.Column(db.Date)
    select_adult = db.Column(db.String)
    select_child = db.Column(db.String)

    def __init__(self, name, last_name, date_from, date_to, select_adult, select_child):
        self.name = name
        self.last_name = last_name
        self.date_from = date_from
        self.date_to = date_to
        self.select_adult = select_adult
        self.select_child = select_child

    # @classmethod
    # def read(cls):
    #     return cls.query.all()

    def add(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f"{self.name} {self.last_name} has reservation from {self.date_from} to {self.date_to} " \
               f"with confirmed adults of {self.select_adult} and {self.select_child} child/ren"


class UserInfo(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String)

    def __init__(self, name, last_name, email):
        self.name = name
        self.last_name = last_name
        self.email = email

    @classmethod
    def read(cls, email):
        return cls.query.filter_by(email=email).first()

    def add(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'you have done great {self.name} {self.last_name} your email is {self.email}'

class RegisteredUsers(db.Model):
    __tablename__ = 'registered_users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String)
    pasword = db.Column(db.String)