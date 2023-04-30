from app.extensions import db


class BaseModel(db.Model):

    __abstract__ = True

    def create(self):
        db.session.add(self)

    def save(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)


