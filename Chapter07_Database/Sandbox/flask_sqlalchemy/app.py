from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

base_directory = path.abspath(path.dirname(__file__))

app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecretkey"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + path.join(base_directory, 'db.sqlite')

db = SQLAlchemy(app)


if __name__ == '__main__':
    from routes import *  # იცოდეთ ეს არ არის სწორი მიდგომა და არასოდეს არ ქნათ, დროებით მაქვს სანამ სტრუქტურიზაციას გავივლით ))
    app.run(debug=True)
