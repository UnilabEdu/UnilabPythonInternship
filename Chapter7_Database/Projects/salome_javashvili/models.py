from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Migrate(app, db)


class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    surname = db.Column(db.String)
    city = db.Column(db.String)
    country = db.Column(db.String)
    company = db.Column(db.String)
    position = db.Column(db.String)
    email = db.Column(db.String)

    def __init__(self, name, surname, city, country, company, position, email):
        self.name = name
        self.surname = surname
        self.city = city
        self.country = country
        self.company = company
        self.position = position
        self.email = email

    def __repr__(self):
        return f'User {self.name} {self.surname} with email {self.email}'

    # Create/ Update
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    # Read
    @classmethod
    def get_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    # delete
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


class PathogenModel(db.Model):
    __tablename__ = 'pathogens'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String)
    genus = db.Column(db.String)
    species = db.Column(db.String)
    strain = db.Column(db.String)
    region = db.Column(db.String)
    year = db.Column(db.Integer)
    sequence = db.relationship('SequenceModel', backref='pathogen', uselist=False)

    def __init__(self, type, genus, species, strain, region, year):
        self.type = type
        self.genus = genus
        self.species = species
        self.strain = strain
        self.region = region
        self.year = year

    def __repr__(self):
        if self.sequence:
            return f'For {self.species} strain {self.strain}, region {self.region}, year {self.year}, sequence is ' \
                   f'available '
        else:
            return f'For {self.species} strain {self.strain}, region {self.region}, year {self.year}, sequence is ' \
                   f'not available '

    # Create/ Update
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    # Read
    @classmethod
    def get_by_species(cls, species):
        return cls.query.filter_by(species=species).first()

    # delete
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


class SequenceModel(db.Model):
    __tablename__ = 'sequences'
    id = db.Column(db.Integer, primary_key=True)
    sequence = db.Column(db.String)
    pathogen_id = db.Column(db.Integer, db.ForeignKey('pathogens.id'))

    def __init__(self, sequence, pathogen_id):
        self.sequence = sequence
        self.pathogen_id = pathogen_id

    def __repr__(self):
        return f'The sequence of pathogen {self.pathogen_id}'

    # Create/ Update
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    # Read
    @classmethod
    def get_by_pathogen_id(cls, pathogen_id):
        return cls.query.filter_by(pathogen_id=pathogen_id).first()

    # delete
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
