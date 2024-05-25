from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about_page():
    return render_template("about.html")

@app.route("/register.html")
def register_page():
    return render_template("register.html")

@app.route("/contact.html")
def contact_page():
    return render_template("contact.html")

@app.route("/products")
def products_page():
    return render_template("products.html")


if __name__=="__main__":
    app.run(debug=True)