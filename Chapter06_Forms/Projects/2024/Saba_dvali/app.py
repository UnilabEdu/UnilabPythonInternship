from flask import Flask, render_template, redirect,url_for
import os
from uuid import uuid4
from data import products
from forms import RegistrationForm, LoginForm


server = Flask(__name__)
server.config["SECRET_KEY"] = "qwert123123123"
# UPLOAD_PATH = os.path.join(server.root_path, "uploads")

validation = False

@server.route("/",methods=["GET", "POST"])
def home():
    global validation
    regform = RegistrationForm()
    logform = LoginForm()
    if regform.validate_on_submit():
        print("reg")
        validation = True
    if logform.validate_on_submit():
        print("log")
        validation = True
        
    return render_template("home.html",products=products.products, regform=regform, logform=logform, validation=validation)


@server.route("/details/<id>")
def details(id):
    for modelkey, modelname in products.products.items():
        for models, product in modelname.items():
            if product["id"] == id:
                prod = product
                return render_template("details.html",prod=prod)
    return redirect(url_for('/'))





if __name__ == "__main__":
    server.run(debug=True, host="0.0.0.0", port=8080)