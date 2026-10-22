
from pydantic import BaseModel


class ProductCreate(BaseModel):

    product_code: str
    product_name: str
    unit_price: float
    available_quantity: int
    active: bool
    category_id : int

class ProductResponse(BaseModel):

    product_code: str
    product_name: str
    unit_price: float
    available_quantity: int
    active: bool
    category_id : int

    class Config:
        from_attributes = True
