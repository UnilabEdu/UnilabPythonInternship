from db import db

class BaseModel:

    def create(self, commit=True):
        db.session.add(self)

        if commit:
            self.save()
        else:
            db.session.flush()
            

    def save(self):
        db.session.commit()


    def delete(self):
        db.session.remove(self)
        db.session.commit()


class Petition(db.Model, BaseModel):

    __tablename__ = "petitions"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    title = db.Column(db.String)
    adress = db.Column(db.String)
    description = db.Column(db.String)
    short_description = db.Column(db.String)
    url_name = db.Column(db.String)
    img1 = db.Column(db.String)
    img2 = db.Column(db.String)
    img3 = db.Column(db.String)
    img4 = db.Column(db.String)
    img5 = db.Column(db.String)
    method = db.Column(db.String)
