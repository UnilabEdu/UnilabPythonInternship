from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_admin import Admin
from flask_migrate import Migrate
from project.admin_models.admin import AdminView

db = SQLAlchemy()
login_manager = LoginManager()
admin = Admin(index_view=AdminView())
migrate = Migrate()
