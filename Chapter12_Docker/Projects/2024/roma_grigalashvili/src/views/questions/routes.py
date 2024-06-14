from flask import render_template, Blueprint, redirect, flash, url_for, request
from os import path
from flask_login import login_required, current_user

from src.views.questions.forms import QuestionForm
from src.models import Question, Quiz
from src.config import Config

TEMPLATES_FOLDER = path.join(Config.BASE_DIRECTORY, "templates", "questions")
question_blueprint = Blueprint("questions", __name__, template_folder=TEMPLATES_FOLDER)

@question_blueprint.route("/questions")
@login_required
def view_questions():
    page = request.args.get('page', 1, type=int)
    per_page = 10  # შეკითხვების რაოდენობა ერთ გვერდზე
    questions = Question.query.join(Quiz).filter(Quiz.user_id == current_user.id).paginate(page=page, per_page=per_page, error_out=False)
    return render_template("questions.html", questions=questions)


@question_blueprint.route('/add_question', methods=['GET', 'POST'])
@login_required
def add_question():
    form = QuestionForm()
    if form.validate_on_submit():
        quiz = Quiz.query.filter_by(id=form.quiz_id.data, user_id=current_user.id).first()
        if not quiz:
            flash('Invalid quiz selected!', 'danger')
            return redirect(url_for('questions.add_question'))
        
        new_question = Question(
            question_text=form.question_text.data,
            choice1=form.choice1.data,
            choice2=form.choice2.data,
            choice3=form.choice3.data,
            choice4=form.choice4.data,
            correct_answer=int(form.correct_answer.data),
            quiz_id=quiz.id
        )
        new_question.create()
        flash('Question added successfully!', 'success')
        return redirect(url_for('questions.view_questions'))
    return render_template('add_question.html', form=form)

@question_blueprint.route('/edit_question/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_question(id):
    question = Question.query.get_or_404(id)
    if question.quiz.user_id != current_user.id:
        flash('You do not have permission to edit this question.', 'danger')
        return redirect(url_for('questions.view_questions'))
    
    form = QuestionForm(obj=question)
    if form.validate_on_submit():
        question.question_text = form.question_text.data
        question.choice1 = form.choice1.data
        question.choice2 = form.choice2.data
        question.choice3 = form.choice3.data
        question.choice4 = form.choice4.data
        question.correct_answer = int(form.correct_answer.data)
        question.save()
        flash('Question updated successfully!', 'success')
        return redirect(url_for('questions.view_questions'))
    return render_template('edit_question.html', form=form, question=question)


@question_blueprint.route('/delete_question/<int:id>', methods=['POST'])
@login_required
def delete_question(id):
    question = Question.query.get_or_404(id)
    if question.quiz.user_id != current_user.id:
        flash('You do not have permission to delete this question.', 'danger')
        return redirect(url_for('questions.view_questions'))
    
    question.delete()
    flash('Question deleted successfully!', 'success')
    return redirect(url_for('questions.view_questions'))