from app.models import UserModel, PostsModel
from app import db

# delete the entire file later


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
