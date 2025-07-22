from pydantic import BaseModel
from typing import Optional
class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    quantity: int


class ProductCreate(ProductBase):
    user_id: int  # this is needed when we will create the product


class Product(ProductBase):
    id: int
    user_id: int
    
class Config:
    orm_mode = True

