from src.admin.base import SecureModelView

class UserView(SecureModelView):
    can_delete = False
    can_create = False

    column_list = ["username", "role"]
    column_labels = {
        "role": "Role"
    }

    form_columns = ["role"]