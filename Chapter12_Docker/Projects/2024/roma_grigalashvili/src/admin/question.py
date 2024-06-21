from wtforms import SelectField
from wtforms.validators import DataRequired
from src.admin.base import SecureModelView
from flask_login import current_user
from flask_admin.model.form import InlineFormAdmin

class QuestionView(SecureModelView):
    # can_view_details = True
    export_types = ["csv"]

    # column_searchable_list = ["category.category"]
    column_list = ["quiz.quiz_name", "question_text", "choice1", "choice2", "choice3", "choice4", "correct_answer_display"]
    column_labels = {
        "quiz.quiz_name": "Quiz",
        "correct_answer_display": "Correct Answer"
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

    # იღებს ბაზიდან სწორი პასუხის შესაბამის ჩანაწერს.
    def _correct_answer_formatter(view, context, model, name):
        return model.get_correct_answer()

    column_formatters = {
        'correct_answer_display': _correct_answer_formatter
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
