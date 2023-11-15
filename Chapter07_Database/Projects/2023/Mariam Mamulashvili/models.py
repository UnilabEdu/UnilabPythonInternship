from db import db

class BaseModel:
    def create(self, commit=True, flush=False):
        db.session.add(self)
        if commit:
            db.session.commit()
        if flush: 
            db.session.flush()


    def save(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Product(db.Model):

    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    product_category = db.Column(db.String)
    page_category = db.Column(db.String)
    image = db.Column(db.String)