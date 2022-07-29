from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate
from forms import LoginForm, DelForm


dirpath = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config["SECRET_KEY"] = "secretkey"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(dirpath, "stu.sqlite")

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
Migrate(app, db)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    email = db.Column(db.String(50))
    password = db.Column(db.Integer)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def post_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f"Student {self.name} created"


if not os.path.isfile("../stu.sqlite"):
    # Created a database if it does not exist and added records
    db.create_all()


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/add", methods=["GET", "POST"])
def add():
    myform = LoginForm()
    if myform.validate_on_submit():
        name = myform.login.data
        email = myform.email.data
        password = myform.password.data
        new_stu = Student(name, email, password)
        new_stu.post_to_db()
        return redirect(url_for("stu_list"))
    return render_template("add_form.html", form=myform)


@app.route("/stu")
def stu_list():
    students = Student.query.all()
    return render_template("stu_list.html", students=students)


@app.route("/delete", methods=['GET', 'POST'])
def delete():

    myform = DelForm()
    print(myform.validate_on_submit())
    if myform.validate_on_submit():
        # name = myform.name.data
        id = myform.id.data
        del_stu = Student.query.get(id)
        # del_stu = Student.query.filter_by(name=name)
        print(del_stu)
        db.session.delete(del_stu)
        db.session.commit()
        return redirect(url_for("stu_list"))

    return render_template("delete.html", form=myform)


if __name__ == "__main__":
    app.run(debug=True)

