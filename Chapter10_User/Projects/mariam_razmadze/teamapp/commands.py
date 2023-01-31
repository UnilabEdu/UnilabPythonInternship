from flask.cli import with_appcontext
import click

from .extensions import db
from teamapp.models.user import User, Role, UserRole
from teamapp.models.question import Question

def init_db():
    db.drop_all()
    db.create_all()

def populate_db():
    users = [{"name": "lim", "password": 'asdf'},
              {"name": "lalo", "password": 'asdf'},
              {"name": "Saul", "password" : 'asdf'},
              {"name": "admin", "password" : 'asdf'}]

    roles = [{"name": "senior"},
             {"name": "junior"},
             {"name": "intern"},]

    click.echo("Creating Users")
    for user in users:
        user = User(name=user['name'], password=user['password'])
        db.session.add(user)

    click.echo("Creating roles")
    for role in roles:
        role = Role(name=role['name'])
        db.session.add(role)
    db.session.flush()

    user_roles = [{'user_id': 1, 'role_id': 1},
                   {'user_id': 2, 'role_id': 2},
                   {'user_id': 3, 'role_id': 3},]

    for user_role in user_roles:
        new_userrole= UserRole(role_id=user_role['role_id'], user_id=user_role['user_id'])
        db.session.add(new_userrole)
    db.session.commit()

    #questions
    questions = [{"question": "What kind of bear is best?", "answer": "black bear", "asked_by_id": 3, 'mentor_id': 1},
                {"question": "Can I fire Jim?", "answer": "black bear", "asked_by_id": 2, 'mentor_id': 1},
                {"question": "Bears or beets?","answer": "Battlestar gallactica",  "asked_by_id": 3, 'mentor_id': 1}]
    
    click.echo("Creating questions")
    for question in questions:
        new_question = Question (question=question['question'], answer=question['answer'], asked_by_id=question['asked_by_id'], mentor_id=question['mentor_id'])
        db.session.add(new_question)

    db.session.commit()

@click.command(name='init_db')
@with_appcontext
def init_db_command():
    click.echo('Creating Database')
    init_db()
    click.echo('Finished Creating Database')

@click.command("populate_db")
@with_appcontext
def populate_db_command():
    populate_db()
  


