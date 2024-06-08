import sys
import os
import pytest
import tempfile

# Ensure the src directory is in the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src import create_app
from src.extensions import admin
from src.config import TestConfig
from src.commands import init_db, populate_db

@pytest.fixture
def app():
    db_fd, db_path = tempfile.mkstemp()
    
    app = create_app(TestConfig)
    app.config.update({"SQLALCHEMY_DATABASE_URI": "sqlite:///" + db_path + ".db"})

    with app.app_context():
        init_db()
        populate_db()
    
    admin._views = []
    yield app

    os.close(db_fd)
    os.unlink(db_path)

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()
