import unittest
import pytest

from src.connections.discount import DiscountConnection


class DiscountConnectionTest(unittest.TestCase):
    mocker = None

    @pytest.fixture(autouse=True)
    def __inject_fixture(self, mocker):
        self.mocker = mocker

    def setUp(self):
        pass

    def test_get_discount_percentage_success(self):
        result = DiscountConnection().get_discount_percentage(product_id=1)
        assert result == 0.5

    def test_get_discount_percentage_raises_error(self):
        with pytest.raises(Exception):
            DiscountConnection().get_discount_percentage(product_id=1)
