import json
import traceback

from pydantic import ValidationError, parse_obj_as

from config.settings import LOGGER
from models.product import ProductModel
from services.cart import CartService
from utils import response_messages
from utils.response_generator import json_response
from utils.exceptions import (
    ProductNotFoundException,
    InvalidProductException,
    EmptyCartException
)


class CartController:

    async def checkout(self, request):
        try:
            body = await request.json()

        except ValueError:
            return json_response(
                messages=[response_messages.INVALID_PAYLOAD],
                status_code=400
            )

        try:
            products = parse_obj_as(list[ProductModel], body.get("products"))
            checkout_cart = CartService().checkout(products=products)
            return json_response(data=checkout_cart.dict())

        except ProductNotFoundException:
            LOGGER.debug("Product not found")
            return json_response(
                messages=[response_messages.PRODUCT_NOT_FOUND],
                status_code=404
            )

        except InvalidProductException:
            LOGGER.debug("Invalid product present in cart")
            return json_response(
                messages=[response_messages.INVALID_PRODUCT],
                status_code=422
            )

        except EmptyCartException:
            LOGGER.debug("Unable to checkout empty cart")
            return json_response(
                messages=[response_messages.EMPTY_CART],
                status_code=422
            )

        except ValidationError as error:
            LOGGER.debug("Payload at request contains validation errors")
            messages = []
            for validation_error in json.loads(error.json()):
                LOGGER.debug(validation_error)
                messages.append({
                    **response_messages.INVALID_FIELD,
                    "field": validation_error['loc'][-1]
                })

            return json_response(messages=messages, status_code=400)

        except Exception as error:
            LOGGER.debug(traceback.format_exc())
            LOGGER.critical(f"Unknown error at checkout endpoint - {error}")
            return json_response(
                messages=[response_messages.UNKNOWN_ERROR],
                status_code=503
            )
