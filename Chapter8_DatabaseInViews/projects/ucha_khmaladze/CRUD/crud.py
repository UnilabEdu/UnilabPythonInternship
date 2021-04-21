

class Crud():

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def read(cls):
        return cls.query.all()

    def delete_from_db(self):
        db.session.delete(self)
        db.commit()
