from src.extensions import db

class BaseModel(db.Model):

    __abstract__ = True

    def create(self, commit=None, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

        if commit is not None:
            self.save_to_db()

    @classmethod
    def read_all(cls):
        return cls.query.all()

    @classmethod
    def read(cls, title):
        return cls.query.filter_by(title=title).first()

    def update(self, commit=None, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

        if commit is not None:
            self.save_to_db()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'Object Name: {self.title}'
