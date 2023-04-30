from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    page_name = "home"
    return render_template("home.html", my_page = page_name)


@app.route("/michael")
def michael():
    page_name = "michael"
    employees = [
        {"number": 1,
         "name": "Dwight",
         "position":"Sales agent"},

        {"number": 2,
         "name": "Pam",
         "position": "Receptionist"},

        {"number": 1,
         "name": "Creed",
         "position": "Something"}

    ]
    return render_template("index.html", my_page = page_name, my_employees =employees)


@app.route("/register")
def register():
    page_name = "register"
    return render_template("registration.html", my_page = page_name)




if __name__ == "__main__":
    app.run(debug=True)