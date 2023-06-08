from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, url_for
from forms import RegisterForm

from os import path
from uuid import uuid4

app = Flask(__name__)
BASE_DIRECTORY = path.abspath(path.dirname(__file__))
app.config["SECRET_KEY"]="NL"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + path.join(BASE_DIRECTORY, "database.db")
db = SQLAlchemy(app)


cards = [
    {"name": "Buckwheat(100g)",
     "description": '350 k/cal'},
    {"name": "Rice(100g)",
     "description": "300 k/cal"}
]

class user_input(db.Model):
    __tabelname__ = "stats"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    weight_input= db.Column(db.String)
@app.route("/",methods=["GET", "POST"])
def nutrition():
    form = RegisterForm()

    if form.validate_on_submit():
        new_user=user_input(username=form.username.data, weight_input=form.goal.data)
        db.session.add(new_user)
        db.session.commit()

    else:
        print(form.errors)

    return render_template("/Nutrition1010.html", form=form)


@app.route("/carbs")
def carbset():
    return render_template("/Carbset.html")


@app.route("/cards")
def macronutrients():
    return render_template("/Cards.html", card_list=cards)


if __name__ == "__main__":
    app.run()
