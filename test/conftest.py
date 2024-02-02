import pytest
from starlette.testclient import TestClient

from app.main import app

@pytest.fixture(scope="function")
def test_app():
    with TestClient(app) as test_client:
        yield test_client
