from project.extensions import db
from project.user.models import BaseModel


class SubsPlan(BaseModel):
    __tablename__ = 'subsplan'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    price = db.Column(db.REAL)
    # user = db.relationship('User', backref='sub_id')

    def __init__(self, name, price):
        self.name = name
        self.price = price


'''
planning to associate relationship after user registers and chooses subscription plan.

for now its functionality is unstable

'''