from flask import Flask, render_template, redirect, flash, session, url_for, request
from forms import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = "goodkey"


@app.route("/", methods=['get', 'POST'])
def home():
    my_form = LoginForm()

    if my_form.validate_on_submit():

        username = my_form.username.data
        password = my_form.password.data
        confirm_pass = my_form.confirm_pass.data
        email = my_form.email.data
        gender = my_form.gender.data

        date = my_form.date.data
        print(date)
        if my_form.file.data:
            my_form.file.data.save('avatar')
        session['username'] = username

        return redirect(url_for("result"))

    errors = [my_form.confirm_pass.errors, my_form.file.errors]
    if errors:
        for error in errors:
            flash(error)

    return render_template("WTForm.html", form=my_form)


@app.route('/result')
def result():
    return render_template("result.html")


if __name__ == "__main__":
    app.run(debug=True)
