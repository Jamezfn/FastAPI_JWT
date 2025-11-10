from passlib.context import CryptContext
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, Request, status

from db_utils.dB import get_db
from utils.token import decode_token
import models

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

class Hash:
    @staticmethod
    def hash(password: str) -> str:
        return pwd_context.hash(password)

    @staticmethod
    def verify(plain_password: str, hashed_password: str) -> bool:
        try:
            return pwd_context.verify(plain_password, hashed_password)
        except Exception as e:
            return False
        
class Authenticate:
    @staticmethod
    def get_current_user(request: Request, db: Session = Depends(get_db)):
        auth = request.headers.get("Authorization").split(" ")[1]
        if not auth:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")
        token = auth.split(" ")[1].strip()
        payload = decode_token(token)
        user_id = payload.get("sub")
        if not user_id:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")
        user =  db.query(models.user.User).filter(models.user.User.id == int(user_id)).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")
        return user
