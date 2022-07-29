from app import db
import os

class BaseModel():
    """
    This Class describe SQLAlchemy DB model with Basic CRUD functionality

    atribs:
        - id: primery key
        - create
        - update
        - delete
        - save
        - read
    """

    def create(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def update_to_db(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_all(cls):
        return cls.query.all()

    def get_by_name(self, name):
        return self.query.filter_by(name=name)


class Student(db.Model, BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    email = db.Column(db.String(50))
    password = db.Column(db.Integer)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password




