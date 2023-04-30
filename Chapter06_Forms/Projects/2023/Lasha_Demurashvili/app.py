from flask import Flask, render_template, request
from forms import RegisterForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecretkey"

users_list = [{"username": "lasha"}, {"username": "gio"}]

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/features")
def features():
    return render_template("features.html")


@app.route("/pricing")
def pricing():
    return render_template("pricing.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/users")
def users():
    return render_template("users.html", users_list=users_list)


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        users = {
            "username": form.username.data
        }
        users_list.append(users)
    print(users_list)
    print(form.errors)

    return render_template("register.html", register_form=form)


if __name__ == "__main__":
    app.run(debug=True)
