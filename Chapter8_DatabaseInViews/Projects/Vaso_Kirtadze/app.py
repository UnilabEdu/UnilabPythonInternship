from flask import Flask, render_template, redirect, url_for, flash
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from form import AddForm, DeleteForm

dirname = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = "VErygoodKEy"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(dirname, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)



class Coach(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(24))
    age = db.Column(db.Integer)




    def create(self, commit=None,  **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

        if commit is not None:
            self.save()

    @classmethod
    def read(cls):
        return cls.query.all()

    def update(self, commit=None,  **kwargs):
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
        return f"Object name {self.name} | {self.age}"



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/create', methods=['GET', 'POST'])
def create():
    my_form = AddForm()

    if my_form.validate_on_submit():
        name = my_form.name.data
        age = my_form.age.data
        coach = Coach()
        coach.create(True, name=name, age=age)
        message = "Coach Added"
        flash(message)
        return redirect(url_for('read'))
    return render_template('create.html', form=my_form)

@app.route('/read')
def read():

    coaches = Coach.read()

    return render_template('read.html', my_coaches=coaches)

@app.route('/update', methods=['GET', 'POST'])
def update():
    my_form = AddForm()
    coaches = Coach.read()

    if my_form.validate_on_submit():

        name = my_form.name.data
        age = my_form.age.data
        coach = Coach.query.filter_by(name=name).first()
        if coach is not None:
            message = "Coach Updated"
            flash(message)
            coach.update(True, age=age)
            return redirect(url_for('read'))
        else:
            message = f"There is no Coach named: {name}, Try again."
            flash(message)
            return redirect(url_for('update'))


    return render_template('update.html', my_coaches=coaches, form=my_form)

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    my_form = DeleteForm()
    coaches = Coach.read()
    if my_form.validate_on_submit():
        name = my_form.name.data
        coach = Coach.query.filter_by(name=name).first()
        if coach is not None:
            message = "Coach Deleted"
            flash(message)
            coach.delete()

        else:
            message = f"There is no Coach named: {name}, Try again."
            flash(message)
            return redirect(url_for('delete'))
        return redirect(url_for('read'))

    return render_template('delete.html', form =my_form, my_coaches=coaches)


if __name__ == '__main__':
    app.run(debug=True)