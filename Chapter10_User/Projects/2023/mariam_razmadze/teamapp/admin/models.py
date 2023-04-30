from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from flask import redirect, url_for
from flask_admin import AdminIndexView

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

class UserModelView(SecureModelView):
    # can_create=False
    # can_edit=False
    # can_export=False
    # can_view_details=False
    column_searchable_list=['name', 'email']
    column_exclude_list=['_password']
    column_list=['name', 'email', 'roles']
    form_excluded_columns=['_password']
    

class QuestionModelView(SecureModelView):
    column_searchable_list=['question', 'answer']
    column_editable_list=['answer']

class RoleModelView(SecureModelView):
    pass