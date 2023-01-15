from flask_admin.contrib.sqla import ModelView
from flask_admin import AdminIndexView
from flask_login import current_user
from flask import redirect, url_for


class SecureModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.has_role("admin")

    def inaccessible_callback(self, name, **kwargs):
        if not self.is_accessible():
            return redirect(url_for('auth.login'))


class SecureAdminView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.has_role("admin")

    def inaccessible_callback(self, name, **kwargs):
        if not self.is_accessible():
            return redirect(url_for('auth.login'))


class ProductModelView(SecureModelView):
    can_delete = False
    can_edit = False
    can_create = False

    column_searchable_list = ["name"]
    column_filters = ["price"]
    can_export = True


class UserModelView(SecureModelView):
    column_searchable_list = ["username", "email"]
    column_list = ["username", "email", "roles"]
    column_editable_list = ["username"]

    form_excluded_columns = ["password"]

