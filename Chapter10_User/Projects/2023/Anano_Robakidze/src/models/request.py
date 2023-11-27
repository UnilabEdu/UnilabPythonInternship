from flask_login import UserMixin

from src.models.base import BaseModel
from src.extentions import db



class Request(BaseModel, UserMixin):

     id = db.Column(db.Integer, primary_key=True)
     message = db.Column(db.String)

     def __repr__(self):
         return self.message