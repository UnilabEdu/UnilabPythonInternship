from flask import Flask, render_template, request, flash
from forms import RegisterForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecretkey"
users = []


@app.route("/")
def melomane():
    return render_template("Melomane.html")



@app.route("/User")
def user():
    return render_template("user.html", users=users)




@app.route("/forms", methods =["GET", "POST"])
def forms():
    form = RegisterForm()
    if form.validate_on_submit():
        user_email = form.email.data
        user_password = form.password.data
        user = {
            "Email": user_email,
            "Password": user_password,
        }
        users.append(user)

        flash("succesfully registered")
    else:
        print(form.errors)

        return render_template("forms.html", register_form=form)


    return render_template("forms.html", register_form=form)

if __name__ == "__main__":
    app.run(debug=True)

