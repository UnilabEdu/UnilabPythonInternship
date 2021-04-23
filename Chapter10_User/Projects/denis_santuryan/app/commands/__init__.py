from flask_migrate import MigrateCommand
from flask_script import Manager, Server

from app import create_app
from .db_init import InitDbCommand

app = create_app()

manager = Manager(app)

manager.add_command('db', MigrateCommand)
manager.add_command('db_init', InitDbCommand)
manager.add_command('runserver', Server(port=5080))
