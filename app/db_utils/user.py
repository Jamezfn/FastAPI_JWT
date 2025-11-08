from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends

import models
from db_utils.dB import get_db
from schemas.auth import UserCreate, UserUpdate
from utils.security import Hash

def create(request: UserCreate, db: Session):
    user_exists = db.query(models.User).filter(models.User.username == request.username).first()
    if user_exists:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists"
        )

    db_user = models.User(
        username=request.username,
        hash_password=Hash.hash(request.password)
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == request.username).first()
    if not user or not Hash.verify(request.password, user.hash_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )
    return user