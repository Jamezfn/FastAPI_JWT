from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends
from datetime import timedelta

import models
from db_utils.dB import get_db
from utils.token import create_token, decode_token
from schemas.auth import TokenResponse, UserCreate, UserUpdate
from utils.security import Hash
from config import settings

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
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Inactive user"
        )
    
    access = create_token(
        subject=user.id,
        token_type="access",
        expires_delta=timedelta(minutes=settings.ACCESS_EXPIRE_MINUTES),
    )

    refresh = create_token(
        subject=user.id,
        token_type="refresh",
        expires_delta=timedelta(days=settings.REFRESH_EXPIRE_DAYS),
    )
    return TokenResponse(
        access_token=access,
        refresh_token=refresh,
        expires_in=settings.ACCESS_EXPIRE_MINUTES * 60,
    )