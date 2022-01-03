import unittest
import pytest

from starlette.testclient import TestClient
from src.utils.response_generator import json_response


class ResponseGeneratorTest(unittest.TestCase):
    mocker = None

    @pytest.fixture(autouse=True)
    def __inject_fixture(self, mocker):
        self.mocker = mocker

    def test_json_response_returns_empty_response(self):
        async def app(scope, receive, send):
            response = json_response()
            await response(scope, receive, send)

        client = TestClient(app)
        response = client.get('/')
        json = response.json()

        assert response.status_code == 200
        assert json["messages"] == []
        assert json["data"] is None

    def test_json_response_returns_dict_data(self):
        async def app(scope, receive, send):
            response = json_response(
                data={"foo": "bar"}
            )
            await response(scope, receive, send)

        client = TestClient(app)
        response = client.get('/')
        json = response.json()

        assert response.status_code == 200
        assert json["messages"] == []
        assert json["data"] == {"foo": "bar"}

    def test_json_response_returns_list_data(self):
        async def app(scope, receive, send):
            response = json_response(
                data=[{"foo": "bar"}]
            )
            await response(scope, receive, send)

        client = TestClient(app)
        response = client.get('/')
        json = response.json()

        assert response.status_code == 200
        assert json["messages"] == []
        assert json["data"] == [{"foo": "bar"}]

    def test_json_response_returns_multiple_messages(self):
        async def app(scope, receive, send):
            response = json_response(
                messages=[
                    {"foo": "bar"},
                    {"test": "test"}
                ]
            )
            await response(scope, receive, send)

        client = TestClient(app)
        response = client.get('/')
        json = response.json()

        assert response.status_code == 200
        assert json["messages"] == [{"foo": "bar"}, {"test": "test"}]
        assert json["data"] is None
