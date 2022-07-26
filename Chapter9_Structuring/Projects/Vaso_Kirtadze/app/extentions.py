
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_admin import Admin


login_manager = LoginManager()


db = SQLAlchemy()
migrate = Migrate()
admin = Admin()