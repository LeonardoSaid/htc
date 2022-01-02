from starlette.applications import Starlette
from starlette.responses import PlainTextResponse
from starlette.routing import Route

from controllers.cart import CartController
from config.settings import BASE_PATH


class Router:

    @staticmethod
    def get_routes():
        return [
            Route(f"{BASE_PATH}/cart/checkout", CartController().checkout, methods=['POST'])
        ]
