from pydantic import BaseModel, Field


class ProductModel(BaseModel):  # pylint: disable=R0903
    id: int
    quantity: int = Field(
        gt=0
    )
