# app/routes/product_routes.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schema import product
from app.db import database
from app.db.user_model import User
from app.auth.auth import get_current_user
from app.crud import product_crud
from app.db.database import get_db

router = APIRouter(prefix="/products", tags=["Products"])

@router.post("/add", response_model=product.Product)
def add_product(
    product_data: product.ProductCreate,
    db: Session = Depends(database.get_db),
    current_user: User = Depends(get_current_user),
):
    return product_crud.create_product(product_data, db, current_user)



@router.get("/get-all-products", response_model=list[product.Product])
def return_all_products(db: Session = Depends(get_db)):
    return product_crud.get_products(db)