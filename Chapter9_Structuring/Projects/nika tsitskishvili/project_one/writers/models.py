from project_one.extensions import db
from project_one.crud import crud

class Writer(db.Model,crud):
    __tablename__ = "writers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    novels = db.relationship("Novel", backref="writer", lazy="dynamic")
    def __init__(self, name):
        self.name = name
    def works(self):
        print("მწერლის ნამუშევრები:")
        for novel in self.novels:
            print(novel.name)
    def __repr__(self):
        return self.name