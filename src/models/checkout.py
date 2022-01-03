from pydantic import BaseModel, Field


class CheckoutProductModel(BaseModel):  # pylint: disable=R0903
    id: int
    quantity: int = Field(
        gt=0
    )
    unit_amount: int
    total_amount: int
    discount: int
    is_gift: bool


class CheckoutCartModel(BaseModel):  # pylint: disable=R0903
    total_amount: int
    total_amount_with_discount: int
    total_discount: int
    products: list[CheckoutProductModel]
