from wtforms import SelectField
from wtforms.validators import DataRequired
from src.admin.base import SecureModelView
from flask_login import current_user
from flask_admin.model.form import InlineFormAdmin

class QuestionView(SecureModelView):
    # can_view_details = True
    export_types = ["csv"]
    create_template = "admin/create_question.html"

    # column_searchable_list = ["category.category"]
    column_list = ["quiz.quiz_name", "question_text", "choice1", "choice2", "choice3", "choice4"]
    column_labels = {
        "quiz.quiz_name": "Quiz"
    }

    # form_columns = ["question_text"]

    # column_labels = {
    #     "category.category": "Category"
    # }

    # if u wana edit without into question
    # column_editable_list = ["choice1", "choice2", "choice3", "choice4"]

    form_overrides = {
        "correct_answer": SelectField
    }
    form_args = {
        "correct_answer": {
            "validators": [DataRequired()],
            "choices": [(1, 'Choice 1'), (2, 'Choice 2'), (3, 'Choice 3'), (4, 'Choice 4')]
        }
    }
    
class QuestionInlineModel(InlineFormAdmin):
    form_columns = ['id', 'question_text', 'choice1', 'choice2', 'choice3', 'choice4', 'correct_answer']
    form_overrides = {
        "correct_answer": SelectField
    }
    form_args = {
        "correct_answer": {
            "validators": [DataRequired()],
            "choices": [(1, 'Choice 1'), (2, 'Choice 2'), (3, 'Choice 3'), (4, 'Choice 4')]
        }
    }
