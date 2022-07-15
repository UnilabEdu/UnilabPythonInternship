from app.extentions import db

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


    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

            self.save()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def save(self):
        db.session.add(self)
        db.session.commit()


class Coach(db.Model, BaseModel):
     __tablename__ = 'coaches'

     name = db.Column(db.String(24))
     age = db.Column(db.Integer)


class Pupil(db.Model, BaseModel):

    __tablename__ = 'pupils'

    name = db.Column(db.String(32))
    is_active = db.Column(db.Boolean, default=True)
    coach_id = db.Column(db.Integer, db.ForeignKey('coaches.id'))

