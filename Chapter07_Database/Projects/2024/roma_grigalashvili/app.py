from flask import Flask, render_template, request, url_for, flash, redirect
from forms import RegisterForm, LoginForm
from os import path
from models import db, Question

app = Flask(__name__)
app.config["SECRET_KEY"] = "kljadskl10248120318znx"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + path.join(app.root_path, "db.sqlite")
db.init_app(app)

# Create the database tables
with app.app_context():
    db.create_all()

top_users_list = [
    {
        "username": "Roma Grigalashvili",
        "gender": "Male",
        "email": "roma.grigalashvili@iliauni.edu.ge",
        "subject": "Math"
    },
    {
        "username": "Saba Dvali",
        "gender": "Male",
        "email": "saba.dvali@iliauni.edu.ge",
        "subject": "History"
    },
    {
        "username": "Tea Godoladze",
        "gender": "Female",
        "email": "tea_godoladze@iliauni.edu.ge",
        "subject": "Math"
    },
    {
        "username": "Roma Grigala",
        "gender": "Male",
        "email": "r.grigalashvili777@gmail.com",
        "subject": "History"
    },
    {
        "username": "Albert Buzaladze",
        "gender": "Male",
        "email": "albert.buzaladze.1@iliauni.edu.ge",
        "subject": "Geography"
    },
]

quiz_list = [
    {
        "question_text":"What is the capital of France?",
        "choice1":"Berlin",
        "choice2":"Madrid",
        "choice3":"Paris",
        "choice4":"Rome",
        "correct_answer":3  # Paris
    }
]

users_list = []

@app.route("/")
def index():
    return render_template("index.html", user_type="admin")

@app.route("/highscores")
def highscores():
    return render_template("highscores.html", top_list=top_users_list)

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = {
            "username": form.username.data,
            "email": form.email.data,
            "password": form.repeat_password.data
        }
        users_list.append(new_user)
        
        flash("Registration successful!", "success")
        print(users_list)
        return redirect(url_for("login"))
    return render_template("register.html", form=form)

@app.route("/questions")
def questions():
    questions = Question.query.all()
    return render_template("questions.html", questions=questions)

@app.route('/add_question', methods=['GET', 'POST'])
def add_question():
    if request.method == 'POST':
        question_text = request.form['question_text']
        choice1 = request.form['choice1']
        choice2 = request.form['choice2']
        choice3 = request.form['choice3']
        choice4 = request.form['choice4']
        correct_answer = int(request.form['correct_answer'])
        
        new_question = Question(
            question_text=question_text,
            choice1=choice1,
            choice2=choice2,
            choice3=choice3,
            choice4=choice4,
            correct_answer=correct_answer
        )
        
        db.session.add(new_question)
        db.session.commit()
        flash("Question added successfully!", "success")
        return redirect(url_for('questions'))
    return render_template('add_question.html')

@app.route('/edit_question/<int:id>', methods=['GET', 'POST'])
def edit_question(id):
    question = Question.query.get_or_404(id)
    if request.method == 'POST':
        question.question_text = request.form['question_text']
        question.choice1 = request.form['choice1']
        question.choice2 = request.form['choice2']
        question.choice3 = request.form['choice3']
        question.choice4 = request.form['choice4']
        question.correct_answer = int(request.form['correct_answer'])
        
        db.session.commit()
        flash('Question updated successfully!', 'success')
        return redirect(url_for('questions'))
    
    return render_template('edit_question.html', question=question)

@app.route('/delete_question/<int:id>', methods=['POST'])
def delete_question(id):
    question = Question.query.get_or_404(id)
    db.session.delete(question)
    db.session.commit()
    flash('Question deleted successfully!', 'success')
    return redirect(url_for('questions'))

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = next((u for u in users_list if u["email"] == form.email.data), None)
        if user and user["password"] == form.password.data:
            flash("Login successful!", "success")
            return redirect(url_for("index"))
        else:
            flash("Login unsuccessful. Please check email and password", "danger")
    return render_template("login.html", form=form)

if __name__ == '__main__':
    app.run(debug=True)
