from flask import Flask, render_template, url_for, flash
from forms import RegisterForm, AboutForm
from flask_sqlalchemy import SQLAlchemy
from os import path

BASE_DIRECTORY = path.abspath(path.dirname(__file__))
app = Flask(__name__)

app.config["SECRET_KEY"] = "abgdevztiklm"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + path.join(BASE_DIRECTORY,"database.db")

db = SQLAlchemy(app)

class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    price = db.Column(db.Integer)

def __repr__(self):
            return f"{self.name}---{self.price}"

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String)

    def __init__(self, username, password):
        self.password = password
        self.username = username

    def __repr__(self):
        return f"შეყვანილი მონაცემებია: {self.usename}{self.password}"

@app.route("/", methods=['GET','POST'])
def index():
    form = RegisterForm()
    if form.validate_on_submit():
        user_username = form.username.data
        user_password = form.password.data
        users = User(username=user_username, password=user_password)
        db.session.add(users)
        db.session.commit()
    else:
        flash("error")
        print(form.errors)
    return render_template("index.html", form=form)

@app.route("/about", methods=['GET','POST'])
def about():
    form = AboutForm()
    if form.validate_on_submit():
       print(form.texstarea.data)
       print(form.texstareatwo.data)
    names = ["fitness", "yoga", "crossfit", "pilates", "judo"]
    return render_template("about.html", list_of_names=names, form=form)



if __name__ == "__main__":
    app.run()



