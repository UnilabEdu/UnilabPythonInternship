from src.admin.base import SecureModelView, SecureIndexView
from flask_admin.form.upload import ImageUploadField
from src.config import Config

from wtforms.validators import DataRequired
from wtforms.fields import SelectField, IntegerField

class WorkView(SecureModelView):

    form_ovverrides = {"product_image" : ImageUploadField,
                        "product_video" : ImageUploadField,
                        "release_year" : IntegerField}


    form_args = {"product_image" : {"base_path": Config.UPLOAD_PATH},
                 "release_year" : {"validators" : [DataRequired()]}}
                        