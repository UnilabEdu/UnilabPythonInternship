from flask.cli import with_appcontext
import click
import csv
from os import path

from src.extensions import db
from src.models import Quiz, Question, Category, User, Role
from src import Config



def init_db():
    click.echo("Creating Database")
    db.drop_all()
    db.create_all()
    click.echo("Database Created")

def populate_db():
    geo_csv_file_path = path.join(Config.BASE_DIRECTORY, "quiz_geography.csv")
    pro_csv_file_path = path.join(Config.BASE_DIRECTORY, "quiz_programming.csv")
    click.echo("Creating Category")
    categories = ["Geography", "Math", "History", "Programming"]
    for category in categories:
        new_category = Category(category=category)
        new_category.create()

    click.echo("Creating First Quiz")
    new_quiz = Quiz(
        quiz_name="Quiz in Geography",
        category_id=int(1))
    new_quiz.create()

    click.echo("Creating Second Quiz")
    new_quiz = Quiz(
        quiz_name="Quiz in Programmig",
        category_id=int(4))
    new_quiz.create()

    with open(geo_csv_file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            new_question = Question(
                question_text=row["question_text"],
                choice1=row["choice1"],
                choice2=row["choice2"],
                choice3=row["choice3"],
                choice4=row["choice4"],
                correct_answer=int(row["correct_answer"]),
                quiz_id=int(row["quiz_id"])
            )
            new_question.create()

    with open(pro_csv_file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            new_question = Question(
                question_text=row["question_text"],
                choice1=row["choice1"],
                choice2=row["choice2"],
                choice3=row["choice3"],
                choice4=row["choice4"],
                correct_answer=int(row["correct_answer"]),
                quiz_id=int(row["quiz_id"])
            )
            new_question.create()

    click.echo("Creating Roles")
    roles = ["admin", "moderator", "member"]
    for role in roles:
        new_role = Role(name=role)
        new_role.create()

    admin_user = User(
        username="Grigala",
        email="roma.grigalashvili@iliauni.edu.ge",
        password="Grigalash1",
        role_id=1
        )
    admin_user.create()

    member_user = User(
        username="Dvali",
        email="saba.dvali.1@iliauni.edu.ge",
        password="Saba.dvali.1"
        )
    member_user.create()


    click.echo("Frist Tables Created")


@click.command("init_db")
@with_appcontext
def init_db_command():
    click.echo("Creating Database")
    init_db()
    click.echo("Database Created")


@click.command("populate_db")
@with_appcontext
def populate_db_command():
    click.echo("Creating Test Populate")
    populate_db()
    click.echo("Test Populate created")