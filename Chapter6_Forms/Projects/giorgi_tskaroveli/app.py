from flask import Flask, render_template, redirect, url_for, session
from forms import registration_form, registration_form2, final_save_to_db
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SECRET_KEY'] = "mySECRETkey"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Migrate(app, db)


class NursesModel(db.Model):
    __tablename__ = "nurses"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    address = db.Column(db.String)
    department = db.Column(db.String)
    shift = db.Column(db.Integer)

    def __init__(self, email, first_name, last_name, address, department, shift):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.department = department
        self.shift = shift

    def __repr__(self):
        return f'Nurse email:{self.email}, name {self.first_name} {self.last_name}, address: {self.address},' \
               f'department: {self.department}, shift: {self.shift}'


@app.route('/step1', methods=['GET', 'POST'])
def step1():
    email = None
    first_name = None
    last_name = None

    form = registration_form()

    if form.validate_on_submit():
        session['email'] = form.email.data
        session['first_name'] = form.first_name.data
        session['last_name'] = form.last_name.data
        return redirect(url_for('step2'))

    return render_template("home.html", form=form, email=email, first_name=first_name, last_name=last_name)


@app.route('/step2', methods=['GET', 'POST'])
def step2():
    address = None
    department = None
    shift = None

    form = registration_form2()

    if form.validate_on_submit():
        session['address'] = form.address.data
        session['department'] = form.department.data
        session['shift'] = form.shift.data

        return redirect(url_for('validation'))

    return render_template("step2.html", form=form, address=address, department=department, shift=shift)


@app.route('/validation', methods=['GET', 'POST'])
def validation():
    form = final_save_to_db()

    if request.method == 'POST':
        print(form.errors)
        new_nurse = NursesModel(session['email'], session['first_name'], session['last_name'],
                                session['address'], session['department'], session['shift'])
        db.session.add(new_nurse)
        db.session.commit()

        return redirect(url_for('step1'))

    return render_template('validation.html', form=form)


if __name__ == '__main__':
    app.run(debug=True, port="4000")
