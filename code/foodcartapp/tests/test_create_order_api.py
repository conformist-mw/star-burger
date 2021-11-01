import pytest
from rest_framework import status

API_ENDPOINT = '/api/order/'


def test_auth_required(client):
    response = client.post(API_ENDPOINT)
    assert response.status_code == status.HTTP_403_FORBIDDEN


def test_get_not_allowed(auth_client):
    response = auth_client.get(API_ENDPOINT)
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED


def test_empty_body(auth_client):
    response = auth_client.post(API_ENDPOINT)
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.parametrize('products', [None, 'string', []])
def test_order_with_wrong_products(auth_client, order, products):
    order['products'] = products
    response = auth_client.post(API_ENDPOINT, data=order)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert len(response.data) == 1
    assert 'products' in response.data


def test_order_created(auth_client, order_with_products):
    response = auth_client.post(API_ENDPOINT, data=order_with_products)
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.parametrize('missing_fields', [
    ['firstname'],
    ['phonenumber', 'lastname'],
    ['firstname', 'lastname', 'phonenumber', 'address'],
])
def test_order_with_missing_fields(
    auth_client, order_with_products, missing_fields,
):
    order = {
        key: value for key, value in order_with_products.items()
        if key not in missing_fields
    }
    response = auth_client.post(API_ENDPOINT, data=order)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert set(response.data) == set(missing_fields)


def test_order_with_null_values(auth_client, order_with_products):
    order = {key: None for key, _ in order_with_products.items()}
    response = auth_client.post(API_ENDPOINT, data=order)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert set(order) == set(response.data)
