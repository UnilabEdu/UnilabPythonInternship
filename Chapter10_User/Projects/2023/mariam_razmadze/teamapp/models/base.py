from teamapp.extensions import db

class BaseModel(db.Model):

    __abstract__=True
    def create(self, commit=True):
        db.session.add(self)
        if commit:
            db.session.commit()
    
    def save(self):
        db.session.commit()