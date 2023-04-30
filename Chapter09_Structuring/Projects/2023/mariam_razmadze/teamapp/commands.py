from flask.cli import with_appcontext
import click

from .extensions import db

@click.command(name='init_db')
@with_appcontext
def init_db():
    click.echo('Creating Database')
    db.drop_all()
    db.create_all()
    click.echo('Finished Creating Database')
