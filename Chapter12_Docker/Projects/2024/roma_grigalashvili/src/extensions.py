from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_admin import Admin

from src.admin.base import SecureAdminIndexView

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
admin = Admin(name="Home", template_mode="bootstrap4", index_view=SecureAdminIndexView(), base_template="admin/admin_base.html")