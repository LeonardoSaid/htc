CART_LIST_EXAMPLE = {
    "products": [
        {
            "id": 1,
            "quantity": 1
        },
        {
            "id": 1,
            "quantity": 1
        }
    ]
}

CART_LIST_INVALID_PRODUCT = {
    "products": [
        {
            "id": 1,
            "quantity": 1
        },
        {
            "id": 6,
            "quantity": 1
        }
    ]
}

CART_LIST_PRODUCT_NOT_FOUND = {
    "products": [
        {
            "id": -1,
            "quantity": 1
        },
        {
            "id": 999,
            "quantity": 1
        }
    ]
}

CART_LIST_EMPTY = {
    "products": []
}
