import unittest
import pytest

from src.connections.discount import DiscountConnection
from src.services.cart import CartService

from tests.unit.fixtures.product import (
    PRODUCT_LIST_NOT_FOUND_EXCEPTION,
    PRODUCT_LIST_INVALID_PRODUCT_EXCEPTION
)
from tests.unit.fixtures.discount import MockStub


class CartServiceTest(unittest.TestCase):
    mocker = None

    @pytest.fixture(autouse=True)
    def __inject_fixture(self, mocker):
        self.mocker = mocker

    def setUp(self):
        def any_function(self, *varargs, **kwargs):  # pylint: disable=W0613
            self.stub = MockStub()

        self.mocker.patch.object(DiscountConnection, "__init__", any_function)

    def test_checkout_raises_empty_cart_exception(self):
        try:
            CartService().checkout(products=[])
        except Exception as error:
            assert type(error).__name__ == "EmptyCartException"

    def test_checkout_raises_product_not_found_exception(self):
        try:
            CartService().checkout(products=PRODUCT_LIST_NOT_FOUND_EXCEPTION)
        except Exception as error:
            assert type(error).__name__ == "ProductNotFoundException"

    def test_checkout_raises_invalid_product_exception(self):
        try:
            CartService().checkout(products=PRODUCT_LIST_INVALID_PRODUCT_EXCEPTION)
        except Exception as error:
            assert type(error).__name__ == "InvalidProductException"
