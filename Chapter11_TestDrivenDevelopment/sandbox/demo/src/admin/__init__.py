from flask_admin import Admin
from src.admin.base import CustomAdminIndexView, SecureModelView
from src.admin.user import UserView
from src.admin.product import ProductView

admin = Admin(name="UniLab Python", template_mode="bootstrap4", index_view=CustomAdminIndexView())