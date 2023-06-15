from market.extensions import db


class BaseModel():
    def create(self, commit=True):
        db.session.add(self)
        if commit:
            self.save()
        else:
            db.session.flush()

    @staticmethod
    def save():
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        self.save()
