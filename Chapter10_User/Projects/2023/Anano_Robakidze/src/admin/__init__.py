from flask_admin import Admin

from src.admin.base import SecureIndexView, SecureModelView
from src.admin.user import UserView
from src.admin.product import ProductView
from src.admin.request import RequestView

admin = Admin(index_view=SecureIndexView(), template_mode="bootstrap4")