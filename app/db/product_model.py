from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base
from typing import Optional 
class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(String(500), nullable=True)
    price = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False)

    # foreign key to User
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    # relationship with User
    owner = relationship("User", back_populates="products")
