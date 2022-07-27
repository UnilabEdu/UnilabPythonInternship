from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Length, Email
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = "key"
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(basedir, "database11000.db")}'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key =True)
    username = db.Column ( db.String(50))
    email = db.Column ( db.String(50))
    password = db.Column(db.String(50))

# db.drop_all()
# db.create_all()



class Login(FlaskForm):
    username1 = StringField('username',validators= [InputRequired(), Length(min = 5, max= 10)])
    password1 = PasswordField('password',validators= [InputRequired(), Length(min = 5, max= 10)])

class RegisterForm(FlaskForm):
        username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
        password = PasswordField('password', validators=[InputRequired(), Length(min=5, max=80)])
        mail = StringField("Email", validators =[InputRequired("Enter your email adress"), Email("Incorect Mail")])

@app.route('/')
def index():
    return render_template('index.html')


#log in
@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = Login()

    if form.validate_on_submit():
        log_data = form.username1.data
        user = User.query.filter_by(username=log_data).first()
        if user:
            if user.password == form.password1.data:
                return  render_template('profile.html', log_data = log_data)
        return "Incorrect username or parssword"

    return render_template('login.html',  form = form)

#sign up

@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    form1 = RegisterForm()
    if form1.validate_on_submit():
        name = form1.username.data
        password = form1.password.data
        email = form1.mail.data

        new_user = User(username = name, email = email, password = password)

        db.session.add(new_user)
        db.session.commit()
        return f"new user has been created"

    return render_template('signup.html', form1 = form1)

@app.route('/profile')
def profile():
    return render_template('profile.html')


if __name__ == '__main__':
    app.run(debug=True)