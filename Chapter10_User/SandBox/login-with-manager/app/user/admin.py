from flask import request, url_for, redirect
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_admin.menu import MenuLink
from flask_user import current_user

from app.models import RandomModel
from app.models.users import User, Role, UserRoles
from app.database import db

admin = Admin(name="Panel", template_mode='bootstrap4')


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


admin.add_view(ModelView(RandomModel, db.session, name="Random"))

admin.add_view(UserModelView(User, db.session, name="User"))
admin.add_view(AdminModelView(Role, db.session, name="Role"))
admin.add_view(AdminModelView(UserRoles, db.session, name="UserRoles"))
admin.add_link(MenuLink(name='Logout', endpoint='user.logout'))
