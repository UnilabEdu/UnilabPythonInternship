from flask_admin.contrib.sqla import ModelView
from flask import url_for, redirect
from app import admin, db
from app.models import UserModel, PostsModel
from app.resources.check_auth import check_auth
from flask_admin import AdminIndexView


class AdminModelView(ModelView):
    def is_accessible(self):
        return check_auth()

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('/'))


class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return check_auth()

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('/'))


admin.add_view(AdminModelView(UserModel, db.session))
admin.add_view(AdminModelView(PostsModel, db.session))
