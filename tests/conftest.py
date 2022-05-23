import os
import warnings

import alembic
import pytest
from starlette.testclient import TestClient
from alembic import command
from alembic.config import Config

from main import app
from core.models import User
from core.main import database
from sqlalchemy_utils import create_database, drop_database


# Apply migrations at beginning and end of testing session
@pytest.fixture(scope="session")
def apply_migrations():
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    os.environ["TESTING"] = "1"
    config = Config("alembic.ini")
    alembic.command.upgrade(config, "head")
    yield
    alembic.command.downgrade(config, "base")


@pytest.fixture(scope="module")
def temp_db():
    create_database(database.SQLALCHEMY_DATABASE_URL)
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    alembic_cfg = Config(os.path.join(base_dir, "alembic.ini"))
    command.upgrade(alembic_cfg, "head")

    try:
        yield database.SQLALCHEMY_DATABASE_URL
    finally:
        drop_database(database.SQLALCHEMY_DATABASE_URL)


# # Create a new application for testing
# @pytest.fixture
# def app(apply_migrations: None) -> FastAPI:
#     from app.api.server import get_application
#     return get_application()
#
#
# # Make requests in our tests
# @pytest.fixture
# async def client(app: FastAPI) -> AsyncClient:
#     async with LifespanManager(app):
#         async with AsyncClient(
#             app=app,
#             base_url="http://testserver",
#             headers={"Content-Type": "application/json"}
#         ) as client:
#             yield client
#

@pytest.fixture(scope='module')
def test_client():
    client = TestClient(app)
    yield client  # testing happens here


@pytest.fixture(scope='module')
def new_user():
    user = User('fullname', 'username', '1234', 'test@test.com')
    return user
