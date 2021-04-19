import os
from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, logout_user, login_required

basedir = os.path.abspath(os.path.dirname(__file__))
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

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


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'ITISHUGESECRET'
    app.config['CSRF_ENABLED'] = True
    app.config['USER_ENABLE_EMAIL'] = False

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    with app.app_context():
        db.create_all()

    login_manager.login_view = 'user.Login'

    from app.book.views import book_blueprint, thank_you_blueprint
    from app.contact.views import contact_blueprint
    from app.registration.views import registration_blueprint

    app.register_blueprint(book_blueprint)
    app.register_blueprint(thank_you_blueprint)
    app.register_blueprint(contact_blueprint)
    app.register_blueprint(registration_blueprint)

    @app.route("/")
    @app.route("/home")
    def home():
        return render_template("home.html", pages=pages)

    @app.route("/rooms")
    def rooms():
        return render_template("room_info.html", pages=pages, table=table)

    return app
