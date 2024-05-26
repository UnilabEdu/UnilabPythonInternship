from flask_admin import Admin
from src.admin.base import SecureModelView, SecureIndexView
from src.admin.product import ProductView
from src.admin.works import WorkView

from flask_login import current_user, logout_user
from flask import redirect, url_for
from flask_admin.menu import MenuLink



admin = Admin(index_view=SecureIndexView(), template_mode="bootstrap4")

class LogoutMenuLink(MenuLink):

    def is_accessible(self):
        return current_user.is_authenticated             

admin.add_link(LogoutMenuLink(name='Logout', category='', url='/logout/'))
