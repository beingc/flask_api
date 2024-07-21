import pytest
from src.app import app as flask_app


@pytest.fixture
def app():
    yield flask_app


@pytest.fixture
def client(app):
    return app.test_client()


def test_api_test_get(client):
    response = client.get('/api/test')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['resultCode'] == '0'
    assert json_data['resultDesc'] == 'Success'
    assert 'id' in json_data['data']
    assert isinstance(json_data['data']['id'], int)


def test_api_test_post_success(client):
    response = client.post('/api/test', json={'id': 123456})
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['resultCode'] == '0'
    assert json_data['resultDesc'] == 'Success'


def test_api_test_post_failure(client):
    response = client.post('/api/test', json={})
    assert response.status_code == 400
    json_data = response.get_json()
    assert json_data['resultCode'] == '-1'
    assert json_data['resultDesc'] == "Failure: 'id' field is missing"
