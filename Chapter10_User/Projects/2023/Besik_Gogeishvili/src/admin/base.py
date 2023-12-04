from flask_admin.contrib.sqla import ModelView
from flask_admin import AdminIndexView
from flask import redirect, url_for
from flask_login import current_user


class SecureModel(ModelView):

    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin()
    

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for("main.error"))


class SecureIndex(AdminIndexView):
    
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin()
    

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for("main.error"))