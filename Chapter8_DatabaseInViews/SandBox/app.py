import os
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from forms import AddForm, DeleteForm

# ფლასკის ობიექტი
app = Flask(__name__)
# კონფიგურაცია ფორმისთვის (არამხოლოდ)
app.config['SECRET_KEY'] = "BestKeptSecret"

# კონფიგურაცია მონაცემთა ბაზისთვის
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(basedir, "data.db")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)


# DB Model
class DBModel(db.Model):
    __tablename__ = "table_1"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    param1 = db.Column(db.Text)
    param2 = db.Column(db.Boolean)

    def __init__(self, name, param1, param2):
        self.name = name
        self.param1 = param1
        self.param2 = param2

    def __repr__(self):
        return f"object named {self.name}"

    # save
    # delete
    # update
    # read


# App Routes
@app.route('/')
def home():
    return render_template('home.html')


# View Forms
@app.route('/add', methods=['GET', 'POST'])
def add_item():
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data
        param1 = form.param1.data
        param2 = bool(form.param2.data)

        item = DBModel(name, param1, param2)
        db.session.add(item)
        db.session.commit()

        return redirect(url_for('list_items'))

    return render_template('add.html', form=form)


@app.route('/list', methods=['GET', 'POST'])
def list_items():
    db_list = DBModel.query.all()
    return render_template('list.html', list_items=db_list)


@app.route('/delete', methods=['GET', 'POST'])
def delete_item():
    form = DeleteForm()

    if form.validate_on_submit():
        item_id = form.id.data
        item = DBModel.query.get(item_id)

        db.session.delete(item)
        db.session.commit()
        return redirect(url_for('list_items'))

    return render_template('delete.html', form = form)


if __name__ == '__main__':
    app.run(debug=True)
