import pytest
import api

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    return app.test_client()


