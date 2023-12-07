from src.extensions import db
from src.models import BaseModel


class Human(BaseModel):
    __tablename__ = "people"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    birth_year = db.Column(db.String)

    def __repr__(self):
        return f"{self.first_name} {self.last_name} (Human)"
