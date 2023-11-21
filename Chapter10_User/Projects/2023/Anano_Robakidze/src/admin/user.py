from src.admin.base import SecureModelView


class UserView(SecureModelView):
    can_create = False
    can_delete = False
    column_list = ["username", "role"]
