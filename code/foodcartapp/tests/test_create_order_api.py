import pytest

API_ENDPOINT = '/api/order/'


def test_auth_required(client):
    response = client.post(API_ENDPOINT)
    assert response.status_code == 403


def test_get_not_allowed(auth_client):
    response = auth_client.get(API_ENDPOINT)
    assert response.status_code == 405


def test_empty_body(auth_client):
    response = auth_client.post(API_ENDPOINT)
    assert response.status_code == 400


@pytest.mark.parametrize('products', [None, 'string', []])
def test_order_with_wrong_products(auth_client, order, products):
    order['products'] = products
    response = auth_client.post(API_ENDPOINT, data=order, format='json')
    assert response.status_code == 400
    assert len(response.data) == 1
    assert 'products' in response.data
