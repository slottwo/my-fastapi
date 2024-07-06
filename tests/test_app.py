from http import HTTPStatus

from fastapi.testclient import TestClient

from my_api.app import app


def test_root():
    client = TestClient(app)  # Arrange

    response = client.get('/')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'ola mundo'}


def test_create_user():
    client = TestClient(app)

    response = client.post(
        '/users/',
        json={
            'username': 'testusername',
            'email': 'test@test.org',
            'password': 'pwd!0123',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'testusername',
        'email': 'test@test.org',
        'id': 1,
    }
