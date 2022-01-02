from datetime import datetime

from config.settings import (
    BLACK_FRIDAY_DATE,
    DISCOUNT_SERVICE_HOST,
    LOGGER
)
from connections.discount import DiscountConnection
from repositories.product import ProductRepository
from utils.exceptions import (
    ServerException,
    ProductNotFoundException,
    InvalidProductException,
    EmptyCartException
)
from models.product import ProductModel
from models.checkout import CheckoutCartModel, CheckoutProductModel


class CartService:

    def checkout(self, products: list[ProductModel]) -> dict:
        if not products:
            raise EmptyCartException

        checkout_cart = CheckoutCartModel(
            total_amount=0,
            total_amount_with_discount=0,
            total_discount=0,
            products=[]
        )
        product_list_info = ProductRepository().get_products()
        discount_connection = DiscountConnection(host=DISCOUNT_SERVICE_HOST)

        for product in products:
            product_info = list(filter(
                lambda item: product.id == item.get("id"), product_list_info
            ))

            if not product_info:
                LOGGER.debug(f"Product not found in database - {product}")
                raise ProductNotFoundException

            elif product_info[0]["is_gift"]:
                LOGGER.debug(f"Gift product found in cart - {product}")
                raise InvalidProductException

            try:
                product_discount_percentage = discount_connection.get_discount_percentage(product.id)
                if not product_discount_percentage:
                    LOGGER.debug(f"No discount percentage found for product id: {product.id}")
                    product_discount_percentage = 0

            except ServerException:
                LOGGER.debug(f"Get discount percentage error for product id: {product.id}")
                product_discount_percentage = 0

            checkout_cart_product = CheckoutProductModel(
                id=product.id,
                quantity=product.quantity,
                unit_amount=product_info[0]["amount"],
                total_amount=product_info[0]["amount"] * product.quantity,
                discount=product_info[0]["amount"] * product.quantity * product_discount_percentage,
                is_gift=False
            )
            checkout_cart.products.append(checkout_cart_product)
            checkout_cart.total_amount += checkout_cart_product.total_amount
            checkout_cart.total_discount += checkout_cart_product.discount
            checkout_cart.total_amount_with_discount += (checkout_cart_product.total_amount -
                                                         checkout_cart_product.discount)

        if datetime.now().strftime("%d/%m/%Y") == BLACK_FRIDAY_DATE:
            LOGGER.debug("Today is black friday, adding gift to cart checkout")
            gift_info = list(filter(
                lambda item: item.get("is_gift"), product_list_info
            ))
            if gift_info:
                gift = CheckoutProductModel(
                    id=gift_info[0]["id"],
                    quantity=1,
                    unit_amount=0,
                    total_amount=0,
                    discount=0,
                    is_gift=True
                )
                checkout_cart.products.append(gift)
                LOGGER.debug(f"Gift with product id {gift_info[0]['id']} added to cart")
            else:
                LOGGER.debug(f"No gift found to add to cart")

        return checkout_cart
