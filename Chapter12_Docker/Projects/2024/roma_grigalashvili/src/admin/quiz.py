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
    form_columns = ["quiz_name", "quiz_text", "category"]

    def is_accessible(self):
        return current_user.is_authenticated and current_user.role.name != "member"

    def get_query(self):
        """Modify the query to show only the quizzes of the current user."""
        query = super(QuizView, self).get_query()
        if current_user.role.name == "admin":
            return query
        return query.filter(self.model.user_id == current_user.id)
        
    def get_count_query(self):
        """Modify the count query to count only the quizzes of the current user."""
        count_query = super(QuizView, self).get_count_query()
        if current_user.role.name == "admin":
            return count_query
        return count_query.filter(self.model.user_id == current_user.id)
    
    def on_model_change(self, form, model, is_created):
        """Set the user_id to the current user's ID when creating or updating a quiz."""
        if is_created:
            model.user_id = current_user.id
        return super(QuizView, self).on_model_change(form, model, is_created)