import click
from flask.cli import with_appcontext
from app.extensions import db
from app.models.users import User


@click.command('makeadmin')
@with_appcontext
def create_test_user():

    click.echo("Started Function")
    admin_user = User(username="Admin", password='Admin', firstname="Mister", lastname="Doe")
    db.session.add(admin_user)
    click.echo("Created User")
    db.session.commit()
    click.echo("Added user to database")