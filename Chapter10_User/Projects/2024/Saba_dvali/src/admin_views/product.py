
from src.admin_views.base import SecureModelView
from wtforms.fields import SelectField


class ProductView(SecureModelView):
    # can_create = False
    can_delete = False
    can_create = False
    can_edit = False
    can_export = True
    export_types = ["csv"]
    
    column_searchable_list = ["product_name","product_model","price","create_time","info"]
    
    column_filters = ["product_name","product_model","price","create_time"] 
    
    # form_overrides = {
    #     "Category": SelectField,
    # }
    
    # form_args = {
    #     "Category": {"choices": ["Apple","Samsung","Google Pixel","Xiaomi","Nokia","Cat","Blackberry","Sony"]}
    # }