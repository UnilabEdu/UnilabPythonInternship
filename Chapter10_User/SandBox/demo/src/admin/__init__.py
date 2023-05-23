from flask_admin import Admin
from src.admin.base import CustomAdminIndexView, SecureModelView

admin = Admin(name="UniLab Python", template_mode="bootstrap4", index_view=CustomAdminIndexView())