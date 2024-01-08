from src.extensions import db
from src.models import BaseModel


class Human(BaseModel):
    __tablename__ = "people"

    id = db.Column(db.Integer, primary_key=True)
    _first_name = db.Column(db.String)
    _last_name = db.Column(db.String)
    birth_year = db.Column(db.String)
    gender = db.Column(db.String)

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value.title()

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value.title()

    def __init__(self, first_name, last_name, birth_year=None, gender=None):
        self._first_name = first_name
        self._last_name = last_name
        self.birth_year = birth_year
        self.gender = gender

    def __repr__(self):
        return f"{self.first_name} {self.last_name} (Human)"
