from flask import Flask, render_template
from templates.items import item_details

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/about")
def about():
    return render_template("about.html")\


@app.route("/items")
def items():
    return render_template("items.html", my_items=item_details)


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/get_started")
def get_started():
    return render_template("pick_one.html")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/sign_up")
def sign_up():
    return render_template("sign_up.html")


@app.route("/random_carousel")
def random_carousel_jumbotron():
    return render_template("random_carousel_jumbotron.html")


@app.route("/discover_manual.html")
def discover_manual():
    return render_template("discover_manual.html")


if __name__ == "__main__":
    app.run(debug=True)

