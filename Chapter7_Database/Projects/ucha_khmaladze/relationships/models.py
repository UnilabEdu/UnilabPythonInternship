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

    __tablename__ = 'workers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    bike = db.relationship('Bike', backref='Worker', uselist=False)
    orders = db.relationship('Order', backref='Worker', lazy='dynamic')

    def __init__(self,name):

        self.name = name

    def __repr__(self):

        if self.bike:
            return f'worker {self.name} is driving {self.bike.model} number {self.bike.id}'
        else:
            return f'worker {self.name} is waiting to assign a bike'

    def report_orders(self):
        print("Orders executed:")
        for order in self.orders:
            print(order.item_name)

class Bike(db.Model):

    __tablename__ = 'bikes'

    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String)
    worker_id = db.Column(db.Integer, db.ForeignKey('workers.id'))

    def __init__(self,model,worker_id):

        self.model = model
        self.worker_id = worker_id

class Order(db.Model):

    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String)
    worker_id = db.Column(db.Integer, db.ForeignKey('workers.id'))

    def __init__(self, item_name, worker_id):

        self.item_name = item_name
        self.worker_id = worker_id

    def __repr__(self):

        return self.item_name

