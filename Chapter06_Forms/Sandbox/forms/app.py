from flask import Flask, render_template, flash
from forms import LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "Chungus"


@app.route('/', methods=['GET', 'POST'])
def home():
    myform = LoginForm()
    if myform.validate_on_submit():
        login = myform.login.data
        password = myform.login.data
        confirmpassword = myform.confirmpassword.data
        email = myform.email.data
        gender = myform.gender.data
        textarea = myform.textarea.data
        submit = myform.submit.data
        print(login, password, email, gender, textarea)

    errors = [myform.login.erros, myform.password.errors]

    if errors:
        for error in errors:
            flash(error)

    return render_template("home.html", form=myform)


if __name__ == '__main__':
    app.run(debug=True)
