from flask_script import Command

from app.data.dummy_data import users, roles
from app.database import db
from app.models import UserModel, Role


class InitDbCommand(Command):
    def run(self):
        init_db()


def init_db():
    db.drop_all()
    db.create_all()
    populate_db()


def populate_db():
    for r in roles:
        r = Role(r)
        db.session.add(r)
    db.session.commit()

    for t in users:
        t = UserModel(*t)
        db.session.add(t)
    db.session.commit()
