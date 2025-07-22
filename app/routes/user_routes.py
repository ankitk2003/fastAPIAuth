from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schema import user
from app.db.database import get_db
from app.crud import user_crud
router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/signup")
def signup(user: user.UserCreate, db: Session = Depends(get_db)):
    print("Incoming User:", user)
    created_user = user_crud.create_user(db, user)
    if created_user is None:
        raise HTTPException(status_code=400, detail="Email already exists")
    return created_user


@router.post("/login")
def login(user: user.UserLogin, db: Session = Depends(get_db)):
    user_token=user_crud.login(user,db)
    return user_token
   