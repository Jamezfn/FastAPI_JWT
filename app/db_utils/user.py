import models
from sqlalchemy.orm import Session
from schemas.auth import UserCreate, UserUpdate
from utils.security import Hash

def create(request: UserCreate, db: Session):
    db_user = models.User(
        username=request.username,
        hash_password=Hash.hash(request.password)
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user