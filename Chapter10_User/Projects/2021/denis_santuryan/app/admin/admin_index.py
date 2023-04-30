from flask import redirect
from flask_admin import AdminIndexView

from app.tools.check_auth import check_auth


class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return check_auth()

    def inaccessible_callback(self, name, **kwargs):
        return redirect('/')
