from project.extensions import db
from flask_login import UserMixin


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

    def is_admin(self):
        return self.role == 'admin'


class User(BaseModel, UserMixin):
    __tablename__ = 'users'


    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(), unique=True)
    password = db.Column(db.String(64))
    gender = db.Column(db.String)
    age = db.Column(db.Integer)
    roles = db.relationship('Role', secondary='user_roles', backref=db.backref('users', lazy='dynamic'))
    profile_pic = db.Column(db.String(), nullable=True)
    about = db.Column(db.String(), nullable=True)

    def has_roles(self, *args):
        return set(args).issubset({role.name for role in self.roles})


class Role(BaseModel):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False, unique=False)

    def __repr__(self):
        return self.name


class UserRoles(BaseModel):
    __tablename__ = 'user_roles'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id', ondelete="CASCADE"))


'''
planning to associate relationship after user registers and chooses subscription plan.

for now its functionality is unstable
'''
