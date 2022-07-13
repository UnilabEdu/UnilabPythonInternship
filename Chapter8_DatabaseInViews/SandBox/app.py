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
    param1 = db.Column(db.Text, default="araferi")
    param2 = db.Column(db.Boolean)

    def create(self, commit=None, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

        if commit is not None:
            self.save()

    @classmethod
    def read(cls, name):
        return cls.query.filter_by(name=name).first()

    def update(self, commit=None, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

        if commit is not None:
            self.save()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f"object named {self.name} | {self.param1} ; {self.param2}"


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

        item = DBModel()
        item.create(name=name, param1=param1, param2=param2, commit=True)
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
        item.delete()
        return redirect(url_for('list_items'))

    return render_template('delete.html', form=form)


@app.route('/update', methods=['GET', 'POST'])
def update_item():
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data
        param1 = form.param1.data
        param2 = bool(form.param2.data)

        item = DBModel.read(name=name)
        item.update(param1=param1, param2=param2, commit=True)
        return redirect(url_for('list_items'))

    return render_template('update.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
