CART_CHECKOUT_EXAMPLE = {
    "data": {
        "total_amount": 30314,
        "total_amount_with_discount": 29557,
        "total_discount": 757,
        "products": [
            {
                "id": 1,
                "quantity": 1,
                "unit_amount": 15157,
                "total_amount": 15157,
                "discount": 0,
                "is_gift": False
            },
            {
                "id": 1,
                "quantity": 1,
                "unit_amount": 15157,
                "total_amount": 15157,
                "discount": 757,
                "is_gift": False
            }
        ]
    },
    "messages": []
}

CART_CHECKOUT_EMPTY_CART_ERROR = {
    "data": None,
    "messages": [
        {
            "code": "E005",
            "description": "Unable to checkout empty cart"
        }
    ]
}

CART_CHECKOUT_PRODUCT_NOT_FOUND_ERROR = {
    "data": None,
    "messages": [
        {
            "code": "E003",
            "description": "Product not found"
        }
    ]
}

CART_CHECKOUT_INVALID_PRODUCT_ERROR = {
    "data": None,
    "messages": [
        {
            "code": "E004",
            "description": "Invalid product in payload"
        }
    ]
}

CART_CHECKOUT_INVALID_QUANTITY_ERROR = {
    "data": None,
    "messages": [
        {
            "code": "E002",
            "description": "Invalid value to field",
            "field": "quantity"
        }
    ]
}

CART_CHECKOUT_INVALID_ID_ERROR = {
    "data": None,
    "messages": [
        {
            "code": "E002",
            "description": "Invalid value to field",
            "field": "id"
        }
    ]
}

CART_CHECKOUT_INVALID_PAYLOAD_ERROR = {
    "data": None,
    "messages": [
        {
            "code": "E001",
            "description": "Invalid body payload"
        }
    ]
}