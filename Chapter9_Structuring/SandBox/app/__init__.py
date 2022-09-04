from flask import Flask
from app.extensions import db, migrate


def create_app(config_file='config.py'):
    application = Flask(__name__)
    application.config.from_pyfile(config_file)
    register_extension(application)
    register_blueprints(application)
    return application


def register_extension(application):
    db.init_app(application)
    migrate.init_app(application, db)


def register_blueprints(application):
    from app.students.views import students_blueprint
    application.register_blueprint(students_blueprint, url_prefix="/students")

    from app.teachers.views import teachers_blueprint
    application.register_blueprint(teachers_blueprint, url_prefix="/teachers")
