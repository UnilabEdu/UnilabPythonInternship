from Chapter9_Structuring.Projects.daniel_gatenadze.Subscription_API.project.extensions import BaseModel
from Chapter9_Structuring.Projects.daniel_gatenadze.Subscription_API.project import db


class SubsPlan(BaseModel):
    __tablename__ = 'subsplan'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    price = db.Column(db.REAL)
    # users = db.relationship('User', backref='sub_id')

    def __init__(self, name, price):
        self.name = name
        self.price = price


'''
planning to associate relationship after user registers and chooses subscription plan.

for now its functionality is unstable

'''