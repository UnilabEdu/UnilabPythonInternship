from flask_admin import Admin
from src.admin.base import SecureModelView, SecureIndexView
from src.admin.product import ProductView
from src.admin.works import WorkView

admin = Admin(index_view=SecureIndexView(), template_mode="bootstrap4")