from functools import wraps
from flask_login import current_user
from flask import redirect, url_for


def admin_required(func):
    @wraps(func)
    def admin_view(*args, **kwargs):
        if current_user and not current_user.has_role("admin"):
            return redirect(url_for("main.index"))
        return func(*args, **kwargs)
    return admin_view
