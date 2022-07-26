from flask_admin.contrib.sqla import ModelView

class Userview(ModelView):
    can_delete = False
    can_create = True
    can_edit = True

    column_exclude_list = ["password_hash"]
    column_searchable_list = ['username', 'email']
    column_filters = ['username']
    column_editable_list = ['username', 'email', 'role']