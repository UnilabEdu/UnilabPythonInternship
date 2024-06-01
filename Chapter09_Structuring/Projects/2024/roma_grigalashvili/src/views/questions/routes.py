from flask import render_template, Blueprint, redirect, flash, url_for
from os import path

from src.views.questions.forms import QuestionForm
from src.models import Question
from src.config import Config

TEMPLATES_FOLDER = path.join(Config.BASE_DIRECTORY, "templates", "questions")
question_blueprint = Blueprint("questions", __name__, template_folder=TEMPLATES_FOLDER)

@question_blueprint.route("/questions")
def questions():
    questions = Question.query.all()
    return render_template("questions.html", questions=questions)


@question_blueprint.route('/add_question', methods=['GET', 'POST'])
def add_question():
    form = QuestionForm()
    if form.validate_on_submit():
        new_question = Question(
            question_text=form.question_text.data,
            choice1=form.choice1.data,
            choice2=form.choice2.data,
            choice3=form.choice3.data,
            choice4=form.choice4.data,
            correct_answer=int(form.correct_answer.data)
        )
        new_question.create()
        flash('Question added successfully!', 'success')
        return redirect(url_for('questions.questions'))
    return render_template('add_question.html', form=form)

@question_blueprint.route('/edit_question/<int:id>', methods=['GET', 'POST'])
def edit_question(id):
    question = Question.query.get_or_404(id)
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
        return redirect(url_for('questions.questions'))
    return render_template('edit_question.html', form=form, question=question)  # Pass the question object


@question_blueprint.route('/delete_question/<int:id>', methods=['POST'])
def delete_question(id):
    question = Question.query.get_or_404(id)
    question.delete()
    flash('Question deleted successfully!', 'success')
    return redirect(url_for('questions.questions'))