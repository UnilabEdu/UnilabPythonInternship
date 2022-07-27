from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class BaseModel(db.Model):
    """
    this class describes sqlalchemy db model  with basic crud functions
    attribs :
        - id : Primary Key

    methods :
        - Create
        - Read
        - Update
        - Delete
        - Save
        - Read_all
    """

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
    def read(cls, name):
        return cls.query.filter_by(name=name).first()  # could use .all()#

        # cls.query.filter(cls.age >= 2)

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
