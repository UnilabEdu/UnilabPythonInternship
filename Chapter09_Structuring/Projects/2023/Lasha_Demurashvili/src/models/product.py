from src.extensions import db


# Products class
class Product(db.Model):
    __tablename__ = "Products"

    id_ = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    price = db.Column(db.Float)
    quantity = db.Column(db.Integer)

    def __repr__(self):
        return f"Product: {self.name}"
