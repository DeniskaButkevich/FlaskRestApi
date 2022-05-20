import os

import pytest
from main import app
from core.models import User
from starlette.testclient import TestClient

from alembic import command
from alembic.config import Config
from core.main import database
from sqlalchemy_utils import create_database, drop_database


@pytest.fixture(scope="module")
def temp_db():
    create_database(database.TEST_SQLALCHEMY_DATABASE_URL) # Создаем БД
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    alembic_cfg = Config(os.path.join(base_dir, "alembic.ini")) # Загружаем конфигурацию alembic
    command.upgrade(alembic_cfg, "head") # выполняем миграции

    try:
        yield database.TEST_SQLALCHEMY_DATABASE_URL
    finally:
        drop_database(database.TEST_SQLALCHEMY_DATABASE_URL) # удаляем БД


@pytest.fixture(scope='module')
def test_client():
    client = TestClient(app)
    yield client  # testing happens here


@pytest.fixture(scope='module')
def new_user():
    user = User('fullname', 'username', '1234', 'test@test.com')
    return user
