from flask import Flask, render_template, flash
from forms import RegisterForm
from flask_sqlalchemy import SQLAlchemy
from os import path

base_directory = path.abspath(path.dirname(__file__))
app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecretkey"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS "] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + path.join(base_directory, "db.sqlite")

db = SQLAlchemy(app)

### Users Class
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)


with app.app_context():
    db.create_all()



@app.route("/")
def melomane():
    return render_template("Melomane.html")



@app.route("/User")
def user():
    users = Users.query.all()

    return render_template("user.html", users=users)




@app.route("/forms", methods =["GET", "POST"])
def forms():
    form = RegisterForm()
    if form.validate_on_submit():
        user_username = form.username.data
        user_email = form.email.data
        user_password = form.password.data
        person = Users(username=user_username, email=user_email, password=user_password)
        db.session.add(person)
        db.session.commit()


        flash("succesfully registered")
    else:
        print(form.errors)

        return render_template("forms.html", register_form=form)


    return render_template("forms.html", register_form=form)

if __name__ == "__main__":
    app.run(debug=True)

