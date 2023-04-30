from app.extentions import db

# DB Model
class BaseModel():

 id = db.Column(db.Integer, primary_key=True)


 def create(self, **kwargs):
     for key, value in kwargs.items():
         setattr(self, key, value)
         self.save()



 @classmethod
 def read_all(cls):
     return cls.query.all()


 @classmethod
 def read(cls, name):
     return cls.query.filter_by(name=name).first()

 def update(self,  **kwargs):
     for key, value in kwargs.items():
         setattr(self, key, value)
         self.save()

 def delete(self):
     db.session.delete(self)
     db.session.commit()

 def save(self):
     db.session.add(self)
     db.session.commit()

 def __repr__(self):
     return f"players name {self.name}"

#new model

class Team(BaseModel, db.Model):
    __tablename__ = "Team"

    name = db.Column(db.String)

class Players(BaseModel, db.Model):
    __tablename__ = "Players"

    name = db.Column(db.String)
    surname  = db.Column(db.Text, default="araferi")
    team = db.Column(db.Text,default="araferi")

