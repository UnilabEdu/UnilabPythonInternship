from flask import Flask, render_template, url_for, flash, redirect
from forms import RegisterForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from os import path 

app = Flask(__name__)
app.config["SECRET_KEY"] = "kljadskl10248120318znx"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + path.join(app.root_path, "db.sqlite")

db=SQLAlchemy(app)

class Top_user(db.Model):
    __tablename__ = "top_user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    subject = db.Column(db.String(50), nullable=False)

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
        "username": "Tea Godoladze",
        "gender": "Female",
        "email": "tea_godoladze@iliauni.edu.ge",
        "subject": "Math"
    },
    {
        "username": "Roma Grigala",
        "gender": "Male",
        "email": "r.grigalashvili777@gmail.com",
        "subject": "History"
    },
    {
        "username": "Albert Buzaladze",
        "gender": "Male",
        "email": "albert.buzaladze.1@iliauni.edu.ge",
        "subject": "Geography"
    },
]

quiz_list = [
    {
        "question_text":"What is the capital of France?",
        "choice1":"Berlin",
        "choice2":"Madrid",
        "choice3":"Paris",
        "choice4":"Rome",
        "correct_answer":3  # Paris
    }
]

users_list = []

@app.before_request
def create_tables():
    db.create_all()
    for user_data in top_users_list:
        if not Top_user.query.filter_by(email=user_data['email']).first():
            user = Top_user(
                username=user_data['username'],
                gender=user_data['gender'],
                email=user_data['email'],
                subject=user_data['subject']
            )
            db.session.add(user)
    db.session.commit()

@app.route("/")
def index():
    return render_template("index.html", user_type="admin")

@app.route("/highscores")
def highscores():
    users = Top_user.query.all()
    top_list = [{'username': user.username, 'gender': user.gender, 'email': user.email, 'subject': user.subject} for user in users]
    return render_template("highscores.html", top_list=top_list)

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

@app.route("/game", methods=["GET", "POST"])
def game():
    return render_template("game.html", quiz=quiz_list)

if __name__ == '__main__':
    app.run(debug=True)
