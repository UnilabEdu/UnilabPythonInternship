from flask import url_for, redirect
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user

from app import admin, db
from app.models import UserModel, PostsModel
from app.tools.check_auth import check_auth


class AdminModelView(ModelView):
    column_exclude_list = ['password', ]

    def is_accessible(self):
        if check_auth():
            if current_user.role_id == 1:
                return True
        return False

    def inaccessible_callback(self, name, **kwargs):
        print(f'{current_user.username} with role "{current_user.role_id} is trying to access an admin-only page"')
        return redirect(url_for('/'))


class ModModelView(ModelView):

    def is_accessible(self):
        if check_auth():
            if current_user.role_id <= 2:
                return True
        return False

    def inaccessible_callback(self, name, **kwargs):
        print(f'{current_user.username} with role "{current_user.role_id} is trying to access a mod-only page"')
        return redirect(url_for('/'))


admin.add_view(AdminModelView(UserModel, db.session))
admin.add_view(ModModelView(PostsModel, db.session))
