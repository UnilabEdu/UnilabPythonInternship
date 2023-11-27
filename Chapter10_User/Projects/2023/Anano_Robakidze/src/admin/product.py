from src.admin.base import SecureModelView
from src.config import Config

from flask_admin.form.upload import ImageUploadField
from wtforms.fields import SelectField



class ProductView(SecureModelView):
    edit_modal = True
    create_modal = True
    can_export = True
    column_editable_list = ["price"]
    column_filters = ["price", "size"]

    column_list = ["title", "price", "color", "size", "img", "category"]


    form_overrides = {"img": ImageUploadField,
                      "size": SelectField,
                      }
    form_args = {"img": {"base_path": Config.UPLOAD_PATH},
                 "size": {"choices": ["S", "M", "L", "XL"]}
                 }



