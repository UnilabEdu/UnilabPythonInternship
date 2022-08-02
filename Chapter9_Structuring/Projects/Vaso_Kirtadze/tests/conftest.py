import os
import tempfile

import pytest
from app import create_app
from app.extentions import db
from app.commands import init_db


@pytest.fixture()
def app():

    db_fd, db_path = tempfile.mkstemp()

    app = create_app()
    app.config.update({
        'TESTING' : True,
        'SQLALCHEMY_DATABASE_URI' : 'sqlite:///' + db_path + '.sqlite',
        'WTF_CSRF_ENABLED': False
    })
    with app.app_context():
        init_db()


    yield app



@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
