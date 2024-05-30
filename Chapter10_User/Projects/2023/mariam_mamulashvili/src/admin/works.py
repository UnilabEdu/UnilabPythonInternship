from src.admin.base import SecureModelView, SecureIndexView
from flask_admin.form.upload import ImageUploadField,  FileUploadField
from src.config import Config

from wtforms.validators import DataRequired
from wtforms.fields import SelectField, IntegerField

class WorkView(SecureModelView):

    edit_modal = True
    create_modal = True

    form_overrides = {"product_image" : ImageUploadField,
                       "product_video" : FileUploadField, 
                       "release_year" : SelectField}


    form_args = {"product_image" : {"base_path": Config.UPLOAD_PATH},
                 "product_video" : {"base_path": Config.UPLOAD_PATH},
                 "release_year" : {"validators" : [DataRequired()]}}
                        