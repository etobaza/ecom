import pytest
from django.contrib.auth.models import User
from django.test import Client


@pytest.mark.django_db
def test_user_authentication():
    client = Client()
    user = User.objects.create_user(
        username='abobus', password='123')
    response = client.post(
        '/api/token/', {'username': 'abobus', 'password': '123'})
    assert response.status_code == 200
    assert 'access' in response.json()


@pytest.mark.django_db
def test_user_authentication_failure():
    client = Client()
    response = client.post(
        '/api/token/', {'username': 'abobus', 'password': '1234'})
    assert response.status_code == 401
    assert 'detail' in response.json()
    assert response.json()[
        'detail'] == 'No active account found with the given credentials'
