from flask import request, url_for, redirect, abort
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_admin.menu import MenuLink
from flask_user import current_user

from app.models.random import RandomModel
from app.models.users import User, Role, UserRoles
from app.models import db


class UserModelView(ModelView):
    column_exclude_list = ['password', ]

    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('user.login', next=request.url))


class AdminModelView(ModelView):
    column_exclude_list = ['password', ]

    def is_accessible(self):
        return current_user.has_role('Admin')

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('user.login', next=request.url))


class MyAdminIndexView(AdminIndexView):
    column_exclude_list = ['password', ]

    def is_accessible(self):
        return current_user.has_role('Admin')

    def inaccessible_callback(self, name, **kwargs):
        abort(403)


admin = Admin(name="Panel", template_mode='bootstrap4', index_view=MyAdminIndexView())

admin.add_view(ModelView(RandomModel, db.session, name="Random"))

admin.add_view(AdminModelView(User, db.session, name="Users", category='User Managements'))
admin.add_view(AdminModelView(Role, db.session, name="User Roles", category='User Managements'))

admin.add_link(MenuLink(name='Logout', endpoint='user.logout'))