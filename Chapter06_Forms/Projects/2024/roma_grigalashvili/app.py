from flask import Flask, render_template, url_for, flash, redirect
from forms import RegisterForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "kljadskl10248120318znx"

top_users_list = [
    {
        "username": "Roma Grigalashvili",
        "gender": "Male",
        "email": "roma.grigalashvili@iliauni.edu.ge",
        "subject": "Math"
    },
    {
        "username": "Saba Dvali",
        "gender": "Male",
        "email": "saba.dvali@iliauni.edu.ge",
        "subject": "History"
    },
    {
        "username": "Saba Dvali",
        "gender": "Male",
        "email": "saba.dvali@iliauni.edu.ge",
        "subject": "History"
    },
    {
        "username": "Saba Dvali",
        "gender": "Male",
        "email": "saba.dvali@iliauni.edu.ge",
        "subject": "History"
    },
    {
        "username": "Roma Grigalashili",
        "gender": "Male",
        "email": "roma.grigalashvili@iliauni.edu.ge",
        "subject": "Geography"
    },
]

users_list = []

@app.route("/")
def index():
    return render_template("index.html", user_type="admin")

@app.route("/highscores")
def highscores():
    return render_template("highscores.html", top_list=top_users_list)

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = {
            "username": form.username.data,
            "email": form.email.data,
            "password": form.repeat_password.data,
            "remember": form.remember.data
        }
        users_list.append(new_user)
        
        flash("Registration successful!", "success")
        print(users)
        return redirect(url_for("users"))
    return render_template("register.html", form=form)

@app.route("/users")
def users():
    return render_template("users.html", users=users_list)

if __name__ == '__main__':
    app.run(debug=True)
