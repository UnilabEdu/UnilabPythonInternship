from src.admin.base import SecureModelView
from flask_login import current_user
from flask import redirect, url_for


class RequestView(SecureModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        if not self.is_accessible():
            return redirect(url_for('auth.login'))
