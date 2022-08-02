from flask_admin.contrib.sqla import ModelView
from flask import redirect, url_for
from flask_login import current_user

class Userview(ModelView):

    def is_accessible(self):
        return True

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('public.home_page'))


    can_delete = False
    can_create = True
    can_edit = True

    column_exclude_list = ["password_hash"]
    column_searchable_list = ['username', 'email']
    column_filters = ['username']
    column_editable_list = ['username', 'email', 'role']
    column_list = ['id', 'username', 'email', 'role']
