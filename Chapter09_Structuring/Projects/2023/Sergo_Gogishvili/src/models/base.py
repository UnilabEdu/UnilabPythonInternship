from src.extensions import db

class BaseModel():
    def create(self):
        db.session.add(self)