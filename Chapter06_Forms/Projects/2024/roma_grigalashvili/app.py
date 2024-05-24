from flask import Flask, render_template, url_for, flash, redirect
from forms import RegisterForm, LoginForm

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
            "password": form.repeat_password.data
        }
        users_list.append(new_user)
        
        flash("Registration successful!", "success")
        print(users)
        return redirect(url_for("login"))
    return render_template("register.html", form=form)

@app.route("/users")
def users():
    print(users_list)
    return render_template("users.html", users=users_list)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = next((u for u in users_list if u["email"] == form.email.data), None)
        if user and user["password"] == form.password.data:
            flash("Login successful!", "success")
            return redirect(url_for("index"))
        else:
            flash("Login unsuccessful. Please check email and password", "danger")
    return render_template("login.html", form=form)

if __name__ == '__main__':
    app.run(debug=True)
