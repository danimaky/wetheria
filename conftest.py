import pytest
from wetheria.app import create_app


@pytest.fixture
def app():
    app = create_app()
    yield app
