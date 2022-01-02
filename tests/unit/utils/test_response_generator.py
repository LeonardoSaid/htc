import unittest
import pytest


class ResponseGeneratorTest(unittest.TestCase):
    mocker = None

    @pytest.fixture(autouse=True)
    def __inject_fixture(self, mocker):
        self.mocker = mocker

    def setUp(self):
        pass

    def test_get_discount_percentage_success(self):
        pass

    def test_get_discount_percentage_raises_error(self):
        pass
