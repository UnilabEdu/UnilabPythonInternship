from flask import Flask, render_template
from forms import LoginForm
app = Flask(__name__)
app.config["SECRET_KEY"] = "ablabdabdab"

@app.route("/", methods=["GET","POST"])
def index():
    myform = LoginForm()
    if myform.validate_on_submit():
        login = myform.login.data
        email = myform.email.data
        password = myform.password.data
        confirmpassword = myform.confirmpassword.data
        gender = myform.gender.data

    return render_template("index.html", form=myform)

@app.route("/home",methods=['GET','POST'])
def home():
    return render_template("home_page.html")

@app.route("/about")
def about():
    return render_template("about_page.html")

if __name__ == "__main__":
    app.run()