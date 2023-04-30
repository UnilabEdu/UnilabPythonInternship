import os
import tempfile

import pytest
from teamapp import create_app, admin
from teamapp.commands import init_db, populate_db

@pytest.fixture
def app():
    db_fd, db_path = tempfile.mkstemp()
    app = create_app()
    admin._views=[]
    app.config.update({
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///' + db_path + '.sqlite',
        'WTF_CSRF_ENABLED': False
    })

    with app.app_context():
        init_db()
        populate_db()

    # print('Creating db')
    yield app

    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()
