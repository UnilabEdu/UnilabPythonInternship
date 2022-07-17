from project_one.extensions import db
from project_one.crud import crud
class Reader(db.Model,crud):
    __tablename__ = "readers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name
