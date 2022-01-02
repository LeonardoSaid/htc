from pydantic import BaseModel, Field


class ProductModel(BaseModel):
    id: int
    quantity: int = Field(
        gt=0
    )
