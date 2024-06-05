from src.views.admin_views import SecureModelView

class ProductView(SecureModelView):
    column_searchable_list = ["name"]
    column_filters = ["price"]
    column_labels = {"name":"სახელი,",
                     "price":"ფასი"}
    create_modal = True
    edit_modal = True
    export_types = ["csv"]
    can_export = True