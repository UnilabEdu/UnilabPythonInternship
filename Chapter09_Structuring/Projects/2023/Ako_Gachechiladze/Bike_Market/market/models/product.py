from market.extensions import db
from market.models.base import BaseModel


class Product(db.Model, BaseModel):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    part = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String)

    owner_id = db.Column(db.ForeignKey("users.id"))
    owner = db.relationship("User", uselist=False)

    def __repr__(self):
        return f"Part: {self.part}, Name:{self.name}"
