import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, "data.sqlite")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)


class Worker(db.Model):
    __tablename__ = "workers"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String)
    # One to One
    bike = db.relationship('Bike', backref='worker', uselist=False)

    # One to Many
    orders = db.relationship('Order', backref='worker', lazy="dynamic")

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        if self.bike:
            return f"მძღოლი {self.name} ატარებს ბაიკს {self.bike.model} ნომრით {self.bike.id}"
        else:
            return f"მძღოლი {self.name} ელოდება თავის ბაიკს"

    def report_orders(self):
        print("დღეს მიტანილი ამანათები:")
        for order in self.orders:
            print(order.item_name)


class Bike(db.Model):
    __tablename__ = "bikes"

    id = db.Column(db.Integer, primary_key=True)

    model = db.Column(db.String)

    # Foreign Key = <Primary Key Table>.<Primary Key Attribute>
    worker_id = db.Column(db.Integer, db.ForeignKey('workers.id'))

    def __init__(self, model, worker_id):
        self.model = model
        self.worker_id = worker_id


class Order(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String)
    worker_id = db.Column(db.Integer, db.ForeignKey('workers.id'))

    def __init__(self, item, worker_id):
        self.item_name = item
        self.worker_id = worker_id

    def __repr__(self):
        return self.item_name
