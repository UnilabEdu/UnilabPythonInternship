from flask import Flask, render_template, request, flash
from forms import RegisterForm
import sqlite3

app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecretkey"
users = []


@app.route("/")
def melomane():
    return render_template("Melomane.html")



@app.route("/User")
def user():
    connection = sqlite3.connect("db.sqlite")
    cursor = connection.cursor()
    users = cursor.execute("SELECT * FROM users").fetchall()


    return render_template("user.html", users=users)




@app.route("/forms", methods =["GET", "POST"])
def forms():
    form = RegisterForm()
    connection = sqlite3.connect("db.sqlite")
    cursor = connection.cursor()

    if form.validate_on_submit():
        cursor.execute("INSERT INTO users VALUES(?,?)", [form.email.data, form.password.data])
        connection.commit()
        connection.close


        flash("succesfully registered")
    else:
        print(form.errors)

        return render_template("forms.html", register_form=form)


    return render_template("forms.html", register_form=form)

if __name__ == "__main__":
    app.run(debug=True)

