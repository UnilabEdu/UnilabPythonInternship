from src.admin.base import SecureModelView


class UserView(SecureModelView):

    can_create = False
    can_delete = False
    edit_modal = True

    column_searchable_list = ["username"]
    column_list = ["username", "gender", "birthdate", "role"]
    column_filters = ["gender"]
    column_labels = {"username": "სახელი", "birthdate": "დაბადების თარიღი", "gender": "სქესი", "role": "ტიპი"}
