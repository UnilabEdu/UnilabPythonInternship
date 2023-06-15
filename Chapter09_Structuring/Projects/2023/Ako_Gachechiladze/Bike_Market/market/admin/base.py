from flask_admin import AdminIndexView
from flask_login import current_user
from flask import redirect, url_for
from flask_admin.contrib.sqla import ModelView


class SecureModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.role.name == "admin"

    def inaccessible_callback(self, name, **kwargs):
        if not self.is_accessible():
            return redirect(url_for("main.home"))


class CustomAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.role.name == "admin"

    def inaccessible_callback(self, name, **kwargs):
        if not self.is_accessible():
            return redirect(url_for("main.home"))
