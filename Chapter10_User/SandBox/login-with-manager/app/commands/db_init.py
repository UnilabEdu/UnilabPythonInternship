from flask_script import Command
from app.database import db
from app.data.dummy import dummy_data
from app.models import RandomModel
from app.models.users import User, Role, UserRoles


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

    admin_role = find_or_create_role("Admin")

    find_or_create_user(
        email="admin@mail.com",
        password="password",
        first_name="admin",
        last_name="adminashvili",
        role=admin_role,
    )

    find_or_create_user(
        email="user@mail.com",
        password="password",
        first_name="user",
        last_name="userisdze"
    )

    db.session.commit()


def find_or_create_item(**kwargs):
    db_item = RandomModel.query.filter_by(param1=kwargs['param1']).first()

    if not db_item:
        db_item = RandomModel(**kwargs)

        db.session.add(db_item)

    return db_item


def find_or_create_role(name):
    role = Role.query.filter_by(name=name).first()

    if not role:
        role = Role(name)

        db.session.add(role)

    return role


def find_or_create_user(email, password, first_name, last_name, role=None):
    user = User.query.filter_by(email=email).first()

    if not user:
        user = User(email=email,
                    password=password,
                    first_name=first_name,
                    last_name=last_name)

        if role:
            user.roles.append(role)
            print(user.roles)

        db.session.add(user)

    return user
