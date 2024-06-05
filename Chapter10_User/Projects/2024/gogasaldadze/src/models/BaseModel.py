from src.ext import db

class BaseMod():
    def create(self):

        db.session.add(self)
        self.save()

    def delete(self):
        db.session.delete(self)
        self.save()

    @staticmethod
    def save():
        db.session.commit()

