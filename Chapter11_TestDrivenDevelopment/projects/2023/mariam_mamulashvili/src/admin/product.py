from src.admin.base import SecureModelView, SecureIndexView
from flask_admin.form.upload import ImageUploadField, FileUploadField
from src.config import Config

from wtforms.validators import DataRequired
from wtforms.fields import SelectField


class ProductView(SecureModelView):
    

    

    form_overrides = {"product_image" : ImageUploadField,
                        "product_video" : FileUploadField,
                        "product_category" : SelectField,
                        "page_category" : SelectField}


    form_args = {"product_image" : {"base_path": Config.UPLOAD_PATH}, 
                 "product_name" : {"validators" : [DataRequired()]},
                 "product_category" : { "choices" : ['video', 'image']},
                 "page_category" : { "choices" : ['gallery', 'gimbal', 'pyrotechnics', 'model_making', 'prosthetics', 'atmospherics']}}
                                                                                