from flask.cli import with_appcontext
import click

from src.extensions import db
from src.models import Question, Category, User, Role



@click.command("init_db")
@with_appcontext
def init_db():
    click.echo("Creating Database")
    db.drop_all()
    db.create_all()
    click.echo("Database Created")

@click.command("populate_db")
@with_appcontext
def populate_db():
    click.echo("Creating Category")
    categories = ["Geography", "Math", "History"]
    for category in categories:
        new_category = Category(category=category)
        new_category.create()

    click.echo("Creating First Question")
    new_question = Question(
        question_text="What is the capital of Germany?",
        choice1="Berlin",
        choice2="Madrid",
        choice3="Paris",
        choice4="Rome",
        correct_answer=int(1),
        category_id=int(1))
    new_question.create()

    click.echo("Creating Roles")
    roles = ["admin", "moderator", "member"]
    for role in roles:
        new_role = Role(name=role)
        new_role.create()

    admin_user = User(
        username="Grigala",
        email="roma.grigalashvili@iliauni.edu.ge",
        password="Grigala27",
        role_id=1
        )
    admin_user.create()

    member_user = User(
        username="Dvali",
        email="saba.dvali.1@iliauni.edu.ge",
        password="Saba.dvali.1",
        role_id=3
        )
    member_user.create()


    click.echo("Frist Tables Created")