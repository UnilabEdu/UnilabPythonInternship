from src.admin.base import SecureModelView


class UserView(SecureModelView):
    column_exclude_list = ["_password"]
    column_labels = {"username":"სახელი", "birthdate":"დაბადების თარიღი", "gender":"სქესი"}
    column_searchable_list = ["username"]