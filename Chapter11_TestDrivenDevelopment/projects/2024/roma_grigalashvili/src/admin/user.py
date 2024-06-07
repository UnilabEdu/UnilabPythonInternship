from src.admin.base import SecureModelView

class UserView(SecureModelView):
    can_delete = False
    can_create = False

    column_list = ["username", "role"]
    column_labels = {
        "role": "Role"
    }

    column_editable_list = ["role"]
    form_columns = ["role"]