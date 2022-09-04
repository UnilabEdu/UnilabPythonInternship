from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.fileadmin import FileAdmin
from flask_admin import AdminIndexView
from flask_login import current_user
from flask import redirect, url_for, request


class AdminView(AdminIndexView):

    def is_accessible(self):
        return current_user.has_roles('admin')

    def inaccessible_callback(self, name, **kwargs):
        if not self.is_accessible():
            return redirect(url_for('auth.log_in', next=request.url))


class UserView(ModelView):
    def is_accessible(self):
        return current_user.has_roles('admin')

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth.log_in'))

    can_create = False
    can_delete = False
    can_edit = True
    column_exclude_list = ['password', ]
    column_searchable_list = ['username', 'email']
    column_filters = ['roles']
    column_editable_list = ['username', 'email', 'roles']
    can_export = True


class RoleView(ModelView):
    def is_accessible(self):
        return current_user.has_roles('admin')

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth.log_in'))

    can_create = False
    can_delete = False
    can_edit = True
    column_searchable_list = ['name']
    column_filters = ['name']
    column_editable_list = ['name']
    can_export = True


class StaticView(FileAdmin):
    def is_accessible(self):
        return current_user.has_roles('admin')

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth.log_in'))
