from flask import Flask
from app.extentions import db



def create_app(config_file = 'config.py'):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    register_extension(app)
    register_blouprint(app)


    return app

def register_extension(app):
    db.init_app(app)

def register_blouprint(app):
    from app.Players.views import students_blueprint
    # app.register_blueprint(students_blueprint, url_prefix="/add")
    app.register_blueprint(students_blueprint, url_prefix="/")
    # app.register_blueprint(students_blueprint, url_prefix="/1")

    # app.register_blueprint(students_blueprint, url_prefix="/delete")
    # app.register_blueprint(students_blueprint, url_prefix="/update")
    # app.register_blueprint(students_blueprint, url_prefix="/list")