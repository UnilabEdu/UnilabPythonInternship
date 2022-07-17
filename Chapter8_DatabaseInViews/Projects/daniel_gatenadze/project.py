import os
from flask import Flask, render_template, redirect, url_for, request
from forms import LoginForm, RegisterForm, ProfilePage
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Model File #

app = Flask(__name__)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


app = Flask(__name__)
projectdir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(projectdir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "password"


class SubsPlan(db.Model):
    __tablename__ = 'subsplan'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    price = db.Column(db.REAL)
    users = db.relationship('User', backref='sub_id')

    def __init__(self, name, price):
        self.name = name
        self.price = price


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(), unique=True)
    password = db.Column(db.String(64))
    gender = db.Column(db.String)
    age = db.Column(db.Integer)
    subscription_id = db.Column(db.Integer, db.ForeignKey('subsplan.id'))

    # def __init__(self, username, email, password, gender, age):
    #     self.username = username
    #     self.email = email
    #     self.password = password
    #     self.gender = gender
    #     self.age = age

    def create(self, commit=None, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

        if commit is not None:
            self.save()

    @classmethod
    def read(cls, name):
        return cls.query.filter_by(name=name).first()  # could use .all()#

        # cls.query.filter(cls.age >= 2)

    def update(self, commit=None, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

        if commit is not None:
            self.save()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def save(self):
        db.session.add(self)
        db.session.commit()


@app.route("/")
def dashboard():
    return render_template("main.html")


@app.route("/products")
def products():
    return render_template("products.html")


@app.route("/flipacoin")
def flipacoin():
    return render_template("flipacoin.html")


@app.route("/login", methods=['GET', 'POST'])
def log_in():
    myform = LoginForm()
    if request.method == 'POST':
        eml = request.form['eml']
        passw = request.form['passw']

        login = User.query.filter_by(email=eml, password=passw).first()
        if login is not None:
            return redirect(url_for('profile_page'))

    return render_template("log_in.html", form=myform)

    #
    # myform = LoginForm()
    # if myform.validate_on_submit():
    #     email = myform.email.data
    #     password = myform.password.data
    #     # fileupload = myform.fileupload.data.save("file.png")
    #     # print(email, password)
    #     session = ['email', 'fileupload', 'password']
    #     email = session[0]
    #
    #     return redirect(url_for('profile_page'))
    #
    # return render_template("log_in.html", form=myform)


@app.route("/register", methods=['GET', 'POST'])
def sign_up():
    myform = RegisterForm()
    if request.method == 'POST':
        uname = request.form['uname']
        eml = request.form['eml']
        passw = request.form['passw']
        gend = request.form['gend']
        age = request.form['age']

        register = User(username=uname, email=eml, password=passw, gender='gender', age='age')
        db.session.add(register)
        db.session.commit()

        return redirect(url_for('profile_page'))
    return render_template("sign_up.html", form=myform)

    # myform = RegisterForm()
    # if myform.validate_on_submit():
    #     username = myform.username.data
    #     email = myform.email.data
    #     password = myform.password.data
    #     confirmpassword = myform.password.data
    #     gender = myform.gender.data
    #     age = myform.age.data
    #
    #     item = User()
    #     item.create(username=username, email=email, password=password, gender=gender, age=age, commit=True)
    #
    #     # fileupload = myform.fileupload.data.save(f'user_avatars/file.png')
    #     # print(username, email, password, confirmpassword, gender, age)
    #     flask.session = ['username', 'email', 'gender', 'age', 'fileupload']
    #     # username, email, gender, age, fileupload = session[0], session[1], session[2], session[3], session[4]
    #     username = flask.session[0]
    #     email = flask.session[1]
    #     gender = flask.session[2]
    #     age = flask.session[3]
    #     fileupload = flask.session[4]
    #     return redirect(url_for('profile_page'))
    #
    # return render_template("sign_up.html", form=myform)


@app.route("/profile_page")
def profile_page():
    myform = ProfilePage()
    return render_template("profile_page.html", form=myform)


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
