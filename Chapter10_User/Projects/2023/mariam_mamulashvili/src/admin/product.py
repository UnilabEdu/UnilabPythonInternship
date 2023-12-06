from src.admin.base import SecureModelView, SecureIndexView
from flask_admin.form.upload import ImageUploadField
from src.config import Config

from wtforms.validators import DataRequired
from wtforms.fields import SelectField


class ProductView(SecureModelView):
    

    edit_modal = True
    create_modal = True

    form_overrides = {"product_image" : ImageUploadField,
                        "product_video" : ImageUploadField,
                        "product_category" : SelectField,
                        "product_page" : SelectField}


    form_args = {"product_image" : {"base_path": Config.UPLOAD_PATH}, 
                 "product_name" : {"validators" : [DataRequired()]},
                 "product_category" : { "choices" : ['video', 'image']},
                 "page_category" : { "choices" : ['gallery', 'gimbal', 'pyrotechnics', 'model_making', 'prosthetics', 'atmospherics']}}
                                                                                