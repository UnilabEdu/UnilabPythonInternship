from flask import Flask
from os import path


base_directory = path.abspath(path.dirname(__file__))


app = Flask(__name__)
app.config["SECRET_KEY"] = "SECRET"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + path.join(base_directory, "database.db")


NAVBAR_ITEMS = [
    {"endpoint": "main", "title": "Home"},
    {"endpoint": "register_get", "title": "Register"},
    {"endpoint": "login", "title": "Login"},
    {"endpoint": "library_get", "title": "Library"}
]


@app.context_processor
def inject_navbar_items():
    return dict(navbar_items=NAVBAR_ITEMS)


if __name__ == "__main__":
    from routes import *
    app.run(debug=True)
