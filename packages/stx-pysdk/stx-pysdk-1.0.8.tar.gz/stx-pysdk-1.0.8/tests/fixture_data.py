from unittest.mock import MagicMock

import pytest

from stxsdk import Selection
from stxsdk.storage.user_storage import User


@pytest.fixture
def selection():
    return Selection


@pytest.fixture
def user():
    return User


@pytest.fixture
def client():
    class Client:
        def __init__(self):
            self.transport = MagicMock()
            self.transport.headers = None

    return Client
