from src.extensions import db

# ONE - TO - ONE relationship
class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    surname = db.Column(db.String)
    birthdate = db.Column(db.Date)

    idcard_id = db.Column(db.ForeignKey("id_cards.id"))
    idcard = db.relationship("IDCard", back_populates="user")

    def __repr__(self):
        return f"{self.name} {self.surname}"


class IDCard(db.Model):
    __tablename__ = "id_cards"

    id = db.Column(db.Integer, primary_key=True)
    id_number = db.Column(db.String, unique=True)
    creation_date = db.Column(db.Date)
    expiry_date = db.Column(db.Date)

    user = db.relationship("User", back_populates="idcard")

    def __repr__(self):
        return f"პირადობა, ნომრით {self.id_number}"