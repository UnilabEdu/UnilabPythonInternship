from wtforms import SelectField
from wtforms.validators import DataRequired
from src.admin.base import SecureModelView
from flask_login import current_user

class QuestionView(SecureModelView):
    can_export = True
    export_types = ["csv"]
    create_template = "admin/create_question.html"

    column_searchable_list = ["category.category"]

    column_labels = {
        "category.category": "Category"
    }

    column_editable_list = ["choice1", "choice2", "choice3", "choice4", "correct_answer"]

    # form_overrides = {
    #     "correct_answer": SelectField
    # }
    # form_args = {
    #     "correct_answer": {
    #         "validators": [DataRequired()],
    #         "choices": [(1, 'Choice 1'), (2, 'Choice 2'), (3, 'Choice 3'), (4, 'Choice 4')]
    #     }
    # }
    # ვერ გავიგე აქ რა ხდება.

    def is_accessible(self):
        return current_user.is_authenticated
