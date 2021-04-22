from flask_script import Manager
from app import create_app
from flask_migrate import MigrateCommand

manager = Manager(create_app())

manager.add_command('db', MigrateCommand)
