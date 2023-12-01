from src.extensions import db
from src.models.base import BaseModel

class Petition(BaseModel):

    __tablename__ = "petitions"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    title = db.Column(db.String)
    address = db.Column(db.String)
    description = db.Column(db.String)
    short_description = db.Column(db.String)
    url_name = db.Column(db.String)
    img1 = db.Column(db.String)
    img2 = db.Column(db.String)
    img3 = db.Column(db.String)
    img4 = db.Column(db.String)
    img5 = db.Column(db.String)
    method = db.Column(db.String)
    goal = db.Column(db.Integer)
    votes = db.Column(db.Integer)

    signers = db.relationship("Signer", back_populates="petitions", secondary="petition_signer")


    def __repr__(self) -> str:
        return self.url_name
    

class PetitionSigner(BaseModel):

    __tablename__  = "petition_signer"

    id = db.Column(db.Integer, primary_key=True)
    petition_id = db.Column(db.Integer, db.ForeignKey("petitions.id"))
    signer_id = db.Column(db.Integer, db.ForeignKey("signers.id"))


class Signer(BaseModel):

    __tablename__ = "signers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    surname = db.Column(db.String)
    email = db.Column(db.String)
    personal_id = db.Column(db.Integer)
    sex = db.Column(db.String)
    number = db.Column(db.Integer)
    city = db.Column(db.String)
    date = db.Column(db.String)

    petitions = db.relationship("Petition", back_populates="signers", secondary="petition_signer")


    def __repr__(self) -> str:
        return self.personal_id
    