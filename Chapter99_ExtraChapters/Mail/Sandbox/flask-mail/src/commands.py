from flask.cli import with_appcontext
from src.extensions import db
from src.models.user import User
import click


@click.command("init_db")
@with_appcontext
def init_db():
    click.echo("Creating Database")
    db.drop_all()
    db.create_all()
    click.echo("Finished Creating Database")


@click.command("populate_db")
@with_appcontext
def populate_db():
    test_user = User(email="test@mail.com", username="testuser1", password="password123")
    test_user.create()