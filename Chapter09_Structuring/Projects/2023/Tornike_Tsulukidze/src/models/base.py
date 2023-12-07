from src.extensions import db


class BaseModel(db.Model):
    __abstract__ = True

    @staticmethod
    def save(self):
        db.session.commit()

    def create(self, commit=True):
        db.session.add(self)

        if commit:
            self.save()
        else:
            db.session.flush()

    def delete(self):
        db.session.delete(self)
        self.save()
