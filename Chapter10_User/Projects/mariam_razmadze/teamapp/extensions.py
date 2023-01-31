from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from teamapp.admin.models import SecureAdminView

login_manager=LoginManager()
db=SQLAlchemy()
migrate=Migrate()
admin=Admin(name='mariam', template_mode="bootstrap4", index_view=SecureAdminView())