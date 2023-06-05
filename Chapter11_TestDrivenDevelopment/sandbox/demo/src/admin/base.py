from flask_admin.contrib.sqla import ModelView
from flask_admin import AdminIndexView, expose
from flask_login import current_user
from flask import redirect, url_for

from src.models import Product

class SecureModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.role.name == "admin"

    def inaccessible_callback(self, name, **kwargs):
        if not self.is_accessible():
            return redirect(url_for('main.index'))


class CustomAdminIndexView(AdminIndexView):

    @expose("/")
    def index(self):
        product = Product.query.all()
        return self.render("admin/home/index.html", products=product)

    def is_accessible(self):
        return current_user.is_authenticated and current_user.role.name == "admin"

    def inaccessible_callback(self, name, **kwargs):
        if not self.is_accessible():
            return redirect(url_for('main.index'))
