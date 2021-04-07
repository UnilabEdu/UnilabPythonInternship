import os
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from forms import AddForm

app = Flask(__name__)
app.config['SECRET_KEY'] = "bestkeptSecret"

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(basedir, "data.db")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)


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


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/add', methods=['GET', 'POST'])
def add_item():
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data
        param1 = form.param1.data
        param2 = form.param2.data

        print(name, param1, param2)

        return redirect(url_for('home'))

    return render_template('add.html', form=form)


@app.route('/add', methods=['GET', 'POST'])
def list_items():
    db_list = DBModel.query.all()



@app.route('/del', methods=['GET', 'POST'])
def delete_item():
    pass


if __name__ == '__main__':
    app.run(debug=True)
