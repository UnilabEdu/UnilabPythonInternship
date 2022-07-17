from flask import Flask
from project_one.extensions import db
from project_one.config import TConfig
def create_application():
    app = Flask(__name__)
    app.config.from_object(TConfig)
    db.init_app(app)

    from project_one.index.views import index_blueprint
    from project_one.writers.views import writers_blueprint
    from project_one.novels.views import novels_blueprint
    from project_one.readers.views import readers_blueprint

    app.register_blueprint(writers_blueprint, url_prefix="/writers")
    app.register_blueprint(novels_blueprint, url_prefix='/novels')
    app.register_blueprint(readers_blueprint, url_prefix="/readers")
    app.register_blueprint(index_blueprint)

    return app
