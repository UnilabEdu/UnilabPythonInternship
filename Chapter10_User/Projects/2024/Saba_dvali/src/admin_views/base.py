from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from flask import redirect, url_for
from flask_admin import AdminIndexView


class SecureModelView(ModelView):
    
    def is_accessible(self):
        return current_user.is_authenticated and current_user.role == 1
    
    def inaccessible_callback(self, name, **kwargs):
        if not self.is_accessible():
            return redirect(url_for('main.home'))
        
        
class SecureAdminIndexView(AdminIndexView):
        
    def is_accessible(self):
        return current_user.is_authenticated and current_user.role == 1
    
    def inaccessible_callback(self, name, **kwargs):
        if not self.is_accessible():
            return redirect(url_for('main.home'))