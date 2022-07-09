from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def dashboard():
    return render_template("main.html")

@app.route("/products")
def products():
    return render_template("products.html")

@app.route("/flipacoin")
def flipacoin():
    return render_template("flipacoin.html")

@app.route("/login")
def log_in():
    return render_template("log_in.html")

@app.route("/register")
def sign_up():
    return render_template("sign_up.html")


if __name__ == "__main__":
    app.run(debug=True)