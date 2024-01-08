from src.extensions import db
from src.models import BaseModel


class User(BaseModel):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    email_address = db.Column(db.String)
    phone_number = db.Column(db.String)
    password = db.Column(db.String)
    human_id = db.Column(db.Integer, db.ForeignKey("people.id"))

    human = db.relationship("Human", uselist=False)

    def __repr__(self):
        return f"{self.username} (User)"
