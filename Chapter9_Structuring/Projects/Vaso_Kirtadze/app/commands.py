from app.extentions import db
from app.models import User


def init_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

    dummy_user = User("mail@gmail.com", "user", "123")
    dummy_user.save()
