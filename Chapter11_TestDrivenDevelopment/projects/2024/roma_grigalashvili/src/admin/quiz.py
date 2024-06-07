from wtforms import SelectField
from wtforms.validators import DataRequired
from src.admin.base import SecureModelView
from src.admin import QuestionInlineModel
from flask_login import current_user

from src.models import Question

class QuizView(SecureModelView):
    can_export = True
    inline_models = (QuestionInlineModel(Question),)

    column_editable_list = ["status"]

    column_searchable_list = ["category.category"]
    column_list = ["quiz_name", "category.category", "status"]
    column_labels = {
        "category.category": "Category",
        "status": "Status"
    }
    form_columns = ["quiz_name", "category"]

    def is_accessible(self):
        return current_user.is_authenticated and current_user.role.name == "admin"


