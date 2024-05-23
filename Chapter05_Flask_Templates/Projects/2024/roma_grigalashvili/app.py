from flask import Flask, render_template, url_for

app = Flask(__name__)
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

@app.route("/")
def index():
    return render_template("index.html", user_type="admin")


@app.route("/highscores")
def highscores():
    return render_template("highscores.html", top_list=top_users_list)


@app.route("/registration")
def game():
    return render_template("registration.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


if __name__ == '__main__':
    app.run(debug=True)
