from sqlalchemy.orm import Session, joinedload
from app.db import product_model
from app.schema import product
from app.db import database
from app.auth.auth import get_current_user
from app.schema.user import User
from fastapi import Depends


def create_product(
    product: product.ProductCreate,
    db: Session = Depends(database.get_db),
    current_user: User = Depends(get_current_user),
):
    new_product = product_model.Product(
        name=product.name,
        description=product.description,
        price=product.price,
        user_id=current_user.id,
        quantity=product.quantity,
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product


# this returns all the products , just for testing purpose
def get_products(db: Session):
    return db.query(product_model.Product).options(joinedload(product_model.Product.owner)).all()
