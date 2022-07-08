from flask import Flask, render_template
app = Flask(__name__)
app.config["SECRET_KEY"] = "secret key"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home",methods=['GET','POST'])
def home():
    return render_template("home_page.html")

@app.route("/about")
def about():
    return render_template("about_page.html")

if __name__ == "__main__":
    app.run()