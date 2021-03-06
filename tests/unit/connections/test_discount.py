import unittest
import pytest

from src.connections.discount import DiscountConnection

from tests.unit.fixtures.discount import MockStub


class DiscountConnectionTest(unittest.TestCase):
    mocker = None

    @pytest.fixture(autouse=True)
    def __inject_fixture(self, mocker):
        self.mocker = mocker

    def setUp(self):
        def any_function(self, *varargs, **kwargs):  # pylint: disable=W0613
            self.stub = MockStub()

        self.mocker.patch.object(DiscountConnection, "__init__", any_function)

    def test_get_discount_percentage_successfully(self):
        result = DiscountConnection(host="localhost:12345").get_discount_percentage(product_id=1)
        assert result == 0.05

    def test_get_discount_percentage_raises_error(self):
        self.mocker.patch.object(MockStub, 'GetDiscount', side_effect=Exception)
        try:
            DiscountConnection(host="localhost:12345").get_discount_percentage(product_id=1)
        except Exception as error:
            assert type(error).__name__ == "ServerException"
