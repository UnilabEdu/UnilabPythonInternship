import os
from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'ITISHUGESECRET'
db = SQLAlchemy(app)
Migrate(app, db)

pages = (
    ("home", "Home"),
    ("book.book", "Book now"),
    ("rooms", "Rooms"),
    ("contact.contact", "Contact us"),
)

table_headers = ["#", "Room Type", "Price", "Quantity"]

table_rows = (
    (1, "Double", "80$", 20),
    (2, "Triple", "110$", 5),
    (3, "Quadruple", "130$", 5),
    (4, "Family", "150$", 4)
)

table = {
    "headers": table_headers,
    "rows": table_rows
}




from app.book.views import book_blueprint, thank_you_blueprint
from app.contact.views import contact_blueprint

app.register_blueprint(book_blueprint)
app.register_blueprint(thank_you_blueprint)
app.register_blueprint(contact_blueprint)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", pages=pages)

@app.route("/rooms")
def rooms():
    return render_template("room_info.html", pages=pages, table=table)