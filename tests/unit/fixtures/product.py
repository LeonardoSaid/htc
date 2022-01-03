from src.models.product import ProductModel

PRODUCT_REPOSITORY_LIST = [{
    "id": 1,
    "title": "Ergonomic Wooden Pants",
    "description": "Deleniti beatae porro.",
    "amount": 15157,
    "is_gift": False
},
    {
    "id": 2,
    "title": "Ergonomic Cotton Keyboard",
    "description": "Iste est ratione excepturi repellendus adipisci qui.",
    "amount": 93811,
    "is_gift": False
},
    {
    "id": 3,
    "title": "Gorgeous Cotton Chips",
    "description": "Nulla rerum tempore rem.",
    "amount": 60356,
    "is_gift": False
},
    {
    "id": 4,
    "title": "Fantastic Frozen Chair",
    "description": "Et neque debitis omnis quam enim cupiditate.",
    "amount": 56230,
    "is_gift": False
},
    {
    "id": 5,
    "title": "Incredible Concrete Soap",
    "description": "Dolorum nobis temporibus aut dolorem quod qui corrupti.",
    "amount": 42647,
    "is_gift": False
},
    {
    "id": 6,
    "title": "Handcrafted Steel Towels",
    "description": "Nam ea sed animi neque qui non quis iste.",
    "amount": 900,
    "is_gift": True
}]

PRODUCT_MODEL_LIST = [
    ProductModel(
        id=1,
        quantity=1
    ),
    ProductModel(
        id=2,
        quantity=2
    )
]

CHECKOUT_CART_WITH_BLACK_FRIDAY_GIFT = {
    "total_amount": 2000,
    "total_amount_with_discount": 0,
    "total_discount": 0,
    "products": [
        {
            "id": 1,
            "quantity": 1,
            "unit_amount": 1000,
            "total_amount": 1000,
            "discount": 1,
            "is_gift": False
        },
        {
            "id": 1,
            "quantity": 2,
            "unit_amount": 500,
            "total_amount": 1000,
            "discount": 1,
            "is_gift": False
        }
    ]
}

CHECKOUT_CART_WITH_DISCOUNT = {
    "total_amount": 2000,
    "total_amount_with_discount": 0,
    "total_discount": 0,
    "products": [
        {
            "id": 1,
            "quantity": 1,
            "unit_amount": 1000,
            "total_amount": 1000,
            "discount": 1,
            "is_gift": False
        },
        {
            "id": 1,
            "quantity": 2,
            "unit_amount": 500,
            "total_amount": 1000,
            "discount": 1,
            "is_gift": False
        }
    ]
}

CHECKOUT_CART_WITHOUT_DISCOUNT = {
    "total_amount": 2000,
    "total_amount_with_discount": 0,
    "total_discount": 0,
    "products": [
        {
            "id": 1,
            "quantity": 1,
            "unit_amount": 1000,
            "total_amount": 1000,
            "discount": 1,
            "is_gift": False
        },
        {
            "id": 1,
            "quantity": 2,
            "unit_amount": 500,
            "total_amount": 1000,
            "discount": 1,
            "is_gift": False
        }
    ]
}
