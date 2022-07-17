from project_one.extensions import db
from project_one.crud import crud

class Novel(db.Model,crud):
    __tablename__ = "novels"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    writer_id = db.Column(db.Integer, db.ForeignKey('writers.id'), nullable=False)
    def __init__(self, name,writer_id):
        self.name = name
        self.writer_id = writer_id

    def __repr__(self):
        return self.name