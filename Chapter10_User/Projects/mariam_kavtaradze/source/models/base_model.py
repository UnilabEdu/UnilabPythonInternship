from source.extensions import db


class BaseModel(db.Model):
    __abstract__ = True

    def create(self, commit=None, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        if commit is not None:
            self.save()

    @classmethod
    def read_all(cls):
        return cls.query.all()

    @classmethod
    def read_one(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def update(self, commit=None, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

        if commit is not None:
            self.save()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f"User: {self.username}"


