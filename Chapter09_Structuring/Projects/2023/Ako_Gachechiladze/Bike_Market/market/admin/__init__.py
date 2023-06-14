from flask_admin import Admin
from market.admin.base import CustomAdminIndexView, SecureModelView

admin = Admin(name="Bike Market", index_view=CustomAdminIndexView())
