from functools import partial

import pytest
from django.contrib.auth.models import User
from django.core.management import call_command
from rest_framework.test import APIClient

from foodcartapp.models import Product


@pytest.fixture(scope='session')
def django_db_setup(django_db_setup, django_db_blocker):  # noqa: PT004
    with django_db_blocker.unblock():
        call_command('loaddata', 'burgers.json')


@pytest.fixture()
def user(db):
    return User.objects.first()


@pytest.fixture()
def product(db):
    return Product.objects.first()


@pytest.fixture()
def client():
    return APIClient()


@pytest.fixture()
def auth_client(user):
    client = APIClient()
    client.force_login(user=user)
    client.post = partial(client.post, format='json')
    return client


@pytest.fixture()
def order() -> dict:
    return {
        'firstname': 'John',
        'lastname': 'Doe',
        'phonenumber': '+380561000000',
        'address': 'New York',
    }


@pytest.fixture()
def order_with_products(order: dict, product) -> dict:
    order['products'] = [{'product': product.id, 'quantity': 1}]
    return order
