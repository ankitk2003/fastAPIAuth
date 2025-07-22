from pydantic import BaseModel
from typing import Optional, List
from .product import Product


class UserBase(BaseModel):
    email: str
    full_name: Optional[str] = None


class UserLogin(BaseModel):
    email: str
    password: str


class UserCreate(BaseModel):
    email: str
    full_name: Optional[str] = None
    password: str


class User(UserBase):
    id: int
    is_active: int
    products: List[Product] = []

class UserOut(BaseModel):
    id:int
    full_name:str
    email:str

class config:
    orm_mode = True


