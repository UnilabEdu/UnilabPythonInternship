from flask import Flask, render_template, request

app = Flask(__name__)


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


@app.route("/register")
def register():
    return render_template("register.html")


if __name__ == "__main__":
    app.run(debug=True)
