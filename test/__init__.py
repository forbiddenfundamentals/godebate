import pytest

from model import connection
from app import app


@pytest.yield_fixture(scope="function", autouse=True)
def db_setup_teardown():
    yield
    print("!!!! CLEAR")
    connection.drop_database(app.config['DB_NAME'])
