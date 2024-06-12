from src.admin_views.base import SecureModelView

class UserView(SecureModelView):
    create_modal = True
    can_delete = False

    
    column_list = ["name","email","age","phone","role","date_joined"]
    column_searchable_list = ["name","email","age","phone"]
    column_editable_list = ["name","email","phone"]
