from src.extensions import db

class BaseModel(db.Model):
    """
    This Class describes SQLAlchemy DB model with Basic CRUD functionality

    attribs:
        - id : Primary Key

    methods:
        - Create
        - Read All
        - Read
        - Update
        - Delete
        - Save
    """
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)

    def create(self, commit=None, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

        if commit is not None:
            self.save_to_db()

    @classmethod
    def read_all(cls):
        return cls.query.all()

    @classmethod
    def read(cls, param):
        return cls.query.filter_by(param=param).first()

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