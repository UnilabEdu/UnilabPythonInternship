from app.database import db


class RandomModel(db.Model):
    __tablename__ = "randoms"

    id = db.Column(db.Integer, primary_key=True)
    param1 = db.Column(db.String)
    param2 = db.Column(db.String)
    param3 = db.Column(db.String)

    def __init__(self, param1, param2, param3):
        self.param1 = param1
        self.param2 = param2
        self.param3 = param3

    def __repr__(self):
        return self.param1
