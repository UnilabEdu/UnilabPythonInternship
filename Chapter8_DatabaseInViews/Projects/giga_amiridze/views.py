from app import db

class Views:
    def create(self, commit=None, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

        if commit is not None:
            self.save_to_db()

    @classmethod
    def read(cls, first_name):
        return cls.query.filter_by(first_name=first_name).first()

    def update(self, commit=None, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

        if commit is not None:
            self.save_to_db()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
