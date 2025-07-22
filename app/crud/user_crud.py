from sqlalchemy.orm import Session
from app.db import user_model
from app.schema import user
from app.schema import user
from app.auth.auth import hash_password, Depends
from fastapi import HTTPException
from app.auth.auth import verify_password, create_access_token
from app.db.database import get_db


def create_user(db: Session, user: user.UserCreate):
    existing_user = (
        db.query(user_model.User).filter(user_model.User.email == user.email).first()
    )
    if existing_user:
        return None  # handle this in the route

    hashed_password = hash_password(user.password)
    print(hashed_password)
    db_user = user_model.User(
        email=user.email,
        password=hashed_password,
        full_name=user.full_name,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"message": "signed up successfully", "user": db_user}


def login(user: user.UserLogin, db: Session):
    db_user = (
        db.query(user_model.User).filter(user_model.User.email == user.email).first()
    )
    if not db_user or not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = create_access_token(data={"sub": str(db_user.id)})
    return {"access_token": access_token, "token_type": "bearer"}


# this will return all the users , just for testing purpost
def get_users(db: Session):
    return db.query(user_model.User).all()
