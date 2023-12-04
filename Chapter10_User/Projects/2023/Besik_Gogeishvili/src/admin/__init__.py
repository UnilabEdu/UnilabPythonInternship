from flask_admin import Admin
from src.admin.base import SecureIndex, SecureModel

admin = Admin(index_view=SecureIndex(), template_mode="bootstrap4")
