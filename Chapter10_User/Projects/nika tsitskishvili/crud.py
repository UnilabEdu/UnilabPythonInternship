from app import db

class Crud():
    @classmethod
    def create(cls, **kwargs):
        item = cls(**kwargs)
        cls.save(item)

    @classmethod
    def read(cls, **kwargs):
        return cls.query.filter_by(**kwargs).first()
        #cls.query.filter(cls.age >= 2)
    @classmethod
    def update(cls, name, new_name, new_id):
        ob = cls.query.filter_by(name=name).first()
        ob.name = new_name
        if new_id != None:
            ob.writer_id = new_id
        db.session.commit()
    @classmethod
    def delete(cls, name):
        ob = cls.query.filter_by(name=name).first()
        db.session.delete(ob)
        db.session.commit()
    def save(self):
        db.session.add(self)
        db.session.commit()







