from src.extensions import db
from src.models.base import BaseModel



class Contact(BaseModel):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    phone = db.Column(db.String)
    company = db.Column(db.String)
    message = db.Column(db.String)
    

    #create string
    def __repr__(self):
        return '<Contact %r>' % self.name
