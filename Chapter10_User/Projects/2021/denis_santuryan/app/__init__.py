import os
from flask import Flask
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_admin import Admin
from app.admin.admin_index import MyAdminIndexView
from app.database import db

migrate = Migrate()
admin = Admin()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = b"d[12;/[d/2rqpl20rk02KPWDMK923#5U_))%FqwKO^A"
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['CSRF_ENABLED'] = True

    db.init_app(app)
    admin.init_app(app, index_view=MyAdminIndexView())
    login_manager.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)

    login_manager.login_view = '/'

    from app.posts.views import posts_blueprint
    from app.profiles.views import profiles_blueprint
    app.register_blueprint(posts_blueprint, url_prefix="/posts")
    app.register_blueprint(profiles_blueprint, url_prefix="/people")

    app.add_url_rule('/people/<path:filename>',
                     endpoint='people',
                     view_func=app.send_static_file)

    return app
