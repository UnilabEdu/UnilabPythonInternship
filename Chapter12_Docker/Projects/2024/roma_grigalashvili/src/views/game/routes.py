from flask import render_template, flash, Blueprint, redirect, request, url_for, session
from os import path
from datetime import datetime
from flask_login import login_required, current_user
from sqlalchemy.sql.expression import func

from src.models import Question, Quiz, Score, User
from src.config import Config

TEMPLATES_FOLDER = path.join(Config.BASE_DIRECTORY, "templates", "game")
game_blueprint = Blueprint("game", __name__, template_folder=TEMPLATES_FOLDER)


def user_has_completed_quiz(user_id, quiz_id):
    return Score.query.filter_by(user_id=user_id, quiz_id=quiz_id).first() is not None

def question_to_dict(question):
    return {
        'id': question.id,
        'question': question.question_text,
        'choices': [question.choice1, question.choice2, question.choice3, question.choice4],
        'answer': question.correct_answer
    }

@game_blueprint.route('/select_game', methods=['GET', 'POST'])
@login_required
def select_game():

    if 'quiz_id' in session:
         return redirect(url_for('game.game'))

    if request.method == 'POST':
        quiz_id = int(request.form['quiz_id'])

        if current_user and user_has_completed_quiz(current_user.id, quiz_id):
            flash("You have already completed this quiz.", "danger")
            return redirect(url_for('game.select_game'))
        
        session['quiz_id'] = quiz_id
        session.pop('selected_questions', None)
        session.pop('current_question', None)
        session.pop('score', None)

        return redirect(url_for('game.game'))
    
    quizzes = Quiz.query.all()
    return render_template('select_game.html', quizzes=quizzes)


@game_blueprint.route('/game', methods=['GET', 'POST'])
@login_required
def game():
    # როცა ქვიზს ვწერ. დაწერის პროცესში თუ logout გავაკეთე და სხვა იუზერით დავლოგინდი ქვიზს გამაგრძელებინებს 
    # იგივე ადგილიდან სადაც წინა იუზერი გაჩერდა.
    
    if 'quiz_id' not in session:
        return redirect(url_for('game.select_quiz'))
    
    quiz_id = session['quiz_id']
    if 'selected_questions' not in session:
        selected_questions = Question.query.filter_by(quiz_id=quiz_id).order_by(func.random()).limit(10).all()
        session['selected_questions'] = [question_to_dict(q) for q in selected_questions]
        session['current_question'] = 0
        session['score'] = 0

    current_question_index = session.get('current_question', 0)
    selected_questions = session['selected_questions']
    score = session.get('score', 0)

    if current_question_index >= len(selected_questions):
        return redirect(url_for('game.game_end'))

    current_question = selected_questions[current_question_index]

    if request.method == 'POST':
        selected_choice = int(request.form['choice'])
        if selected_choice == current_question['answer']:
            session['score'] += 1

        session['current_question'] += 1
        return redirect(url_for('game.game'))
    
    total_questions = len(selected_questions)
    progress_percentage = int(current_question_index / total_questions * 100)

    return render_template('game.html', question=current_question, score=score, question_num=current_question_index + 1, total_questions=total_questions, progress=progress_percentage, enumerate=enumerate)


@game_blueprint.route('/game_end')
@login_required
def game_end():
    score = session.get('score', 0)
    total_questions = len(session.get('selected_questions', []))

    if current_user:
        new_score = Score(user_id=current_user.id, quiz_id=session['quiz_id'], score=score, date=datetime.now())
        new_score.create()

    session.pop('quiz_id', None)
    session.pop('selected_questions', None)
    session.pop('current_question', None)
    session.pop('score', None)

    return render_template('game_end.html', score=score, total_questions=total_questions)
