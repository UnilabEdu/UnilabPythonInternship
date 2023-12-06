from flask import Flask, render_template, request, redirect
from forms import AddUser, LogUser
app = Flask(__name__)

app.config["SECRET_KEY"] = "argetyviii"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["TRACK_DATABASE_MODIFICATIONS"] = False


if __name__ == '__main__':
    from routes import *
    app.run(debug=True)