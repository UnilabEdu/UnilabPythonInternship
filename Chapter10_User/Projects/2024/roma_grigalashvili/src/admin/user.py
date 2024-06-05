from src.admin.base import SecureModelView

class UserView(SecureModelView):
    can_delete = False
    can_create = False
    can_edit = False

    column_list = ["id", "username", "role.name"] # role არის სხვა ცხრილებში, როგორ გამოვაჩინო?
    column_labels = {
        "role.name": "Role"
    }