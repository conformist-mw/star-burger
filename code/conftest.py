import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient


@pytest.fixture()
def user(db):
    return User.objects.create_user('user')


@pytest.fixture()
def client():
    return APIClient()


@pytest.fixture()
def auth_client(user):
    client = APIClient()
    client.force_login(user=user)
    return client


@pytest.fixture()
def order():
    return {
        'firstname': 'John',
        'lastname': 'Doe',
        'phonenumber': '+380561000000',
        'address': 'New York',
    }
