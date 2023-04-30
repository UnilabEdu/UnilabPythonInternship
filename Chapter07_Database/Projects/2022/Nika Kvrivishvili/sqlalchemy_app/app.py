import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class NameModel(db.Model):
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    sname = db.Column(db.String)

    def __init__(self, name, sname):
        self.name = name
        self.sname = sname

    def create(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def read(cls, self):
        return cls.query.get(self)

    def delete(self):
        db.session.delete(self)

        db.session.commit()


if __name__ == "__main__":
    app.run(debug=True)
