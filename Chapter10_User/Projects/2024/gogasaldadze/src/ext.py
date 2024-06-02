from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_admin import Admin
from flask_migrate import Migrate
from src.views.admin_views.base import SecureAdminIndexview
db= SQLAlchemy()
login_manager = LoginManager()
admin = Admin(index_view=SecureAdminIndexview())
migrate = Migrate()

