from app.models import UserModel, PostsModel
from app import db
# from resources.resources import users


def create(resource, model):
    if type(resource[0]) == list or type(resource[0]) == tuple:
        for u in resource:
            user = model(*u)
            db.session.add(user)
    else:
        user = model(*resource)
        db.session.add(user)
    db.session.commit()


def read(class_name, _id):
    return class_name.query.get(_id)


def read_all(class_name):
    return class_name.query.all()


def update(class_name, username, new_params):
    # works both with username and title (both users and pages)
    try:
        row = class_name.query.filter_by(username=username).first()
        db.session.delete(row)
    except:
        try:
            row = class_name.query.filter_by(username=username).first()
            db.session.delete(row)
        except:
            db.session.add(class_name(*new_params))
            db.session.commit()


def delete(class_name, _id):
    row = class_name.query.get(_id)
    db.session.delete(row)
    db.session.commit()


def add_relationship(class_name, _id, foreign_class_name, foreign_id):
    # adds a last argument to an already existing row
    # doesn't work???
    primary = class_name.query.get(_id)
    foreign = foreign_class_name.query.get(foreign_id)
    primary.users_id = foreign.id
    db.session.add(primary)
    db.session.commit()


def save_to_db(user, attribute, data):
    from app import db
    setattr(user, attribute, data)
    db.session.commit()

# Using CRUD

# create(users, UserModel)
# print(read_all(UserModel))
# update(UserModel, 'denissanturyan', ('denissanturyan', 'Denis Santuryan', 'denis.santuryan.1@iliauni.edu.ge', 21, 'Male', '598-465-865'))
# delete(UserModel, 12)

# add_relationship(PagesModel, 1, UserModel, 2)
