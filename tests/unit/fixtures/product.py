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

PRODUCT_LIST_NOT_FOUND_EXCEPTION = [
    ProductModel(
        id=1,
        quantity=1
    ),
    ProductModel(
        id=2,
        quantity=2
    )
]

PRODUCT_LIST_INVALID_PRODUCT_EXCEPTION = [
    ProductModel(
        id=6,
        quantity=1
    ),
    ProductModel(
        id=2,
        quantity=2
    )
]
