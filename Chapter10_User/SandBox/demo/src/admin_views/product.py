from flask_admin.form import ImageUploadField
from flask_admin.model import InlineFormAdmin
from markupsafe import Markup
from wtforms.fields import SelectField
from flask_login import current_user
from uuid import uuid4
from os import path

from src.admin_views.base import SecureModelView
from src.config import Config
from src.models import ProductImage, UserProduct, User


def generate_filename(obj, file):
    _, extension = path.splitext(file.filename)
    return f"{uuid4()}{extension}"


class ProductImageInline(InlineFormAdmin):
    form_overrides = {"name": ImageUploadField}

    form_args = {
        "name": {"base_path": Config.UPLOAD_DIRECTORY,
                "namegen": generate_filename}
    }


class ProductView(SecureModelView):
    can_export = True
    export_types = ["csv"]
    create_template = "admin/create_product.html"

    column_editable_list = ["price"]
    column_searchable_list = ["name", "description"]
    column_filters = ["price"]
    column_list = ["img", "name", "description", "category", "price", "product_images"]
    column_labels = {"name": "სახელი", "description": "აღწერა", "price": "ფასი", "category": "კატეგორია"}

    column_formatters = {
        "img": lambda v,c,m,n: Markup(f"<img src='/static/{m.img}' width=128>"),
        "product_images": lambda v,c,m,n: len(m.product_images)
    }

    form_overrides = {
        "category": SelectField,
        "img": ImageUploadField
    }

    form_args = {
        "category": {"choices": ["CPU", "GPU", "RAM"]},
        "img": {"base_path": Config.UPLOAD_DIRECTORY,
                "namegen": generate_filename}
    }

    inline_models = [ProductImageInline(ProductImage)]

    def is_accessible(self):
        return current_user.is_authenticated

    def get_query(self):
        if current_user.is_admin():
            return self.session.query(self.model)

