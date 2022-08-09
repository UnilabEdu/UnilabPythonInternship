from src.app import app
import pytest


@pytest.fixture()
def application():
    yield app


my_list = [x for x in range(10)]