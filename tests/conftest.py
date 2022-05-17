import os

import pytest

from app import app, main
from app.model import User


@pytest.fixture(scope='module')
def test_client():
    app.config.from_object(main.settings[os.environ.get('APPLICATION_ENV', 'testing')])

    with app.test_client() as testing_client:
        with app.app_context():
            yield testing_client  # this is where the testing happens!


@pytest.fixture(scope='module')
def new_user():
    user = User('fullname', 'username', '1234', 'test@test.com')
    return user
