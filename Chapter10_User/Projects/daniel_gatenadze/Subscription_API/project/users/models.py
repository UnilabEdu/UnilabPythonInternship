from Chapter10_User.Projects.daniel_gatenadze.Subscription_API.project.extensions import BaseModel
from Chapter10_User.Projects.daniel_gatenadze.Subscription_API.project import db
from flask_login import UserMixin

class User(BaseModel,UserMixin):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(), unique=True)
    password = db.Column(db.String(64))
    gender = db.Column(db.String)
    age = db.Column(db.Integer)
    # subscription_id = db.Column(db.Integer, db.ForeignKey('subsplan.id'))


'''
planning to associate relationship after user registers and chooses subscription plan.

for now its functionality is unstable
'''