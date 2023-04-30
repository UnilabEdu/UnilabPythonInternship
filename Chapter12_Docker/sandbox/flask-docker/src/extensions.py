from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_admin import Admin
from src.admin.models import SecureAdminView

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
admin = Admin(name="Unilab Admin Page", template_mode="bootstrap4", index_view=SecureAdminView())