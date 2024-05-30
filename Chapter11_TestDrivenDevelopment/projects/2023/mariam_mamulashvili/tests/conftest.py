import pytest 
import tempfile
import os

from src import create_app
from src.commands import init_db, populate_db
from src.admin import admin


@pytest.fixture
def app():

    db_fn, db_path = tempfile.mkstemp()

    app = create_app()
    app.config.update({
        "SQLALCHEMY_DATABASE_URI" : f"sqlite:///{db_path}/.sqlite",
        "TESTING": True,
        "WTF_CSRF_ENABLED" : False,
        "DEBUG" : False
    })

    admin._views = []

    with app.app_context():
        init_db()
        populate_db()

    yield app

    os.close(db_fn)
    os.unlink(db_path)


@pytest.fixture 
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()