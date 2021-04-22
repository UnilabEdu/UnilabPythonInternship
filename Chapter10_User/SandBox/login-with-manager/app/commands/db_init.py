from flask_script import Command
from app.database import db
from app.data.dummy import dummy_data
from app.models import RandomModel


class InitDbCommand(Command):

    def run(self):
        init_db()


def init_db():
    db.drop_all()
    db.create_all()
    populate_db()


def populate_db():
    for item in dummy_data:
        find_or_create_item(**item)

    db.session.commit()


def find_or_create_item(**kwargs):
    db_item = RandomModel.query.filter_by(param1=kwargs['param1']).first()

    if not db_item:
        db_item = RandomModel(**kwargs)

        db.session.add(db_item)

    return db_item
