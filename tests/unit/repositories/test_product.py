import unittest
import pytest

from src.repositories.product import ProductRepository
from tests.unit.fixtures.product import PRODUCT_REPOSITORY_LIST


class ProductRepositoryTest(unittest.TestCase):
    mocker = None

    @pytest.fixture(autouse=True)
    def __inject_fixture(self, mocker):
        self.mocker = mocker

    def setUp(self):
        pass

    def test_load_data_and_get_products_successfully(self):
        product_repository = ProductRepository()
        products = product_repository.get_products()
        assert products == PRODUCT_REPOSITORY_LIST
