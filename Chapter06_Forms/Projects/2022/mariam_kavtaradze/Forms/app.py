from flask import Flask, render_template, flash, redirect, url_for, session
from forms import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = "secretkey"

@app.route("/")
def index():
    return render_template("up_index.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    myform = LoginForm()
    if myform.validate_on_submit():
        login = myform.login.data
        email = myform.email.data
        password = myform.password.data
        confirm_password = myform.confirm_password.data
        experience = myform.experience.data
        account_type = myform.account_type.data
        flash("SUCCESS")
        data = [login, email, password, confirm_password, experience, account_type]
        print(data)
        session['data'] = data
        session['username'] = login
        session['email'] = email
        session['experience'] = experience
        print(myform.file_upload.data)
        if myform.file_upload.data:
            myform.file_upload.data.save("file.png")
        return redirect(url_for('success'))
    return render_template("up_register.html", form=myform)


@app.route('/success')
def success():
    return render_template("success.html")


@app.route("/random_carousel")
def random_carousel_jumbotron():
    return render_template("up_random_carousel_jumbotron.html")


@app.route("/discover_manual.html")
def discover_manual():
    return render_template("up_discover_manual.html")


if __name__ == "__main__":
    app.run(debug=True)

