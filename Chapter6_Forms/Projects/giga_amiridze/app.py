from flask import Flask, render_template, session, flash, redirect, url_for
from forms import SignUpForms

app = Flask(__name__)

app.config["SECRET_KEY"] = "my_secret_key"

@app.route('/', methods=['GET', 'POST'])
def home():
    form = SignUpForms()

    if form.validate_on_submit():
        session["first_name"] = form.first_name.data
        session["last_name"] = form.last_name.data
        session["email"] = form.email.data
        session["password"] = form.password.data
        session["confirm_pass"] = form.confirm_pass.data
        session["birth_date"] = form.birth_date.data
        session["gender"] = form.gender.data
        return redirect(url_for("welcome"))

    errors = [form.first_name.errors, form.last_name.errors, form.email.errors, form.password.errors]
    if errors:
        for error in errors:
            flash(error)

    return render_template("index.html", form=form)

@app.route('/welcome')
def welcome():
    return render_template("welcome.html")

if __name__ == "__main__":
    app.run(port=7777, debug=True)