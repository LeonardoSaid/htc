import requests
import unittest
import pytest

from starlette.applications import Starlette
from starlette.testclient import TestClient

from src.router import Router
from tests.integration.fixtures.cart import payload as cart_payload_fixtures
from tests.integration.fixtures.cart import response as cart_response_fixtures


class CartIntegrationTest(unittest.TestCase):
    mocker = None

    @pytest.fixture(autouse=True)
    def __inject_fixture(self, mocker):
        self.mocker = mocker

    def setUp(self):
        self.app = Starlette(debug=True, routes=Router.get_routes())

    def test_cart_checkout_raises_invalid_quantity(self):
        client = TestClient(self.app)
        response = client.post(
            '/cart-management/v1/cart/checkout',
            json=cart_payload_fixtures.CART_LIST_INVALID_QUANTITY
        )

        json = response.json()

        assert response.status_code == 400
        assert json == cart_response_fixtures.CART_CHECKOUT_INVALID_QUANTITY_ERROR

    def test_cart_checkout_raises_invalid_payload(self):
        client = TestClient(self.app)
        response = client.post(
            '/cart-management/v1/cart/checkout',
            json=None
        )

        json = response.json()

        assert response.status_code == 400
        assert json == cart_response_fixtures.CART_CHECKOUT_INVALID_PAYLOAD_ERROR

    def test_cart_checkout_raises_invalid_id(self):
        client = TestClient(self.app)
        response = client.post(
            '/cart-management/v1/cart/checkout',
            json=cart_payload_fixtures.CART_LIST_INVALID_ID
        )

        json = response.json()

        assert response.status_code == 400
        assert json == cart_response_fixtures.CART_CHECKOUT_INVALID_ID_ERROR

    def test_cart_checkout_returns_empty_cart_error(self):
        client = TestClient(self.app)
        response = client.post(
            '/cart-management/v1/cart/checkout',
            json=cart_payload_fixtures.CART_LIST_EMPTY
        )

        json = response.json()

        assert response.status_code == 422
        assert json == cart_response_fixtures.CART_CHECKOUT_EMPTY_CART_ERROR

    def test_cart_checkout_returns_invalid_product_error(self):
        client = TestClient(self.app)
        response = client.post(
            '/cart-management/v1/cart/checkout',
            json=cart_payload_fixtures.CART_LIST_INVALID_PRODUCT
        )

        json = response.json()

        assert response.status_code == 422
        assert json == cart_response_fixtures.CART_CHECKOUT_INVALID_PRODUCT_ERROR

    def test_cart_checkout_returns_product_not_found_error(self):
        client = TestClient(self.app)
        response = client.post(
            '/cart-management/v1/cart/checkout',
            json=cart_payload_fixtures.CART_LIST_PRODUCT_NOT_FOUND
        )

        json = response.json()

        assert response.status_code == 404
        assert json == cart_response_fixtures.CART_CHECKOUT_PRODUCT_NOT_FOUND_ERROR

    def test_cart_checkout_successfully(self):
        client = TestClient(self.app)
        response = client.post(
            '/cart-management/v1/cart/checkout',
            json=cart_payload_fixtures.CART_LIST_EXAMPLE
        )

        json = response.json()
        fixture = cart_response_fixtures.CART_CHECKOUT_EXAMPLE['data']

        assert response.status_code == 200
        assert json['data']['total_amount'] == fixture['total_amount']
        assert len(json['data']['products']) == len(fixture['products'])
        for index, product in enumerate(json['data']['products']):
            product['id'] == fixture['products'][index]['id']
            product['quantity'] == fixture['products'][index]['quantity']
            product['unit_amount'] == fixture['products'][index]['unit_amount']
            product['total_amount'] == fixture['products'][index]['total_amount']
            product['is_gift'] == fixture['products'][index]['is_gift']