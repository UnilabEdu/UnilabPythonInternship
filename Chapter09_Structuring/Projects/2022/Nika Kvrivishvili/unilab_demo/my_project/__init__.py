from flask import Flask
from my_project.extensions import db
from my_project.config import TestConfig


def create_app():

    app = Flask(__name__)
    app.config.from_object(TestConfig)

    db.init_app(app)

    @app.before_first_request
    def create_tables():
        db.create_all()

    from my_project.programs.views import program_blueprint
    from my_project.students.views import students_blueprint
    from my_project.front_end.view import main_blueprint

    app.register_blueprint(students_blueprint, url_prefix="/students")
    app.register_blueprint(program_blueprint, url_prefix='/admin')
    app.register_blueprint(main_blueprint)

    return app
