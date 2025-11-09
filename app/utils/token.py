from typing import Union
import uuid
from datetime import datetime, timedelta, timezone
import jwt
from fastapi import HTTPException, status

from config import settings

def create_token(subject: Union[str, int, uuid.UUID], token_type:str, expires_delta: timedelta) -> str:
    now = datetime.now(timezone.utc)
    exp = now + expires_delta
    jti = uuid.uuid4()

    payload = {
            "sub": str(subject),
            "iat": int(now.timestamp()),
            "exp": int(exp.timestamp()),
            "type": token_type,
            "jti": str(jti),
            }
    return jwt.encode(payload, settings.SECRET, algorithm=settings.ALGORITHM)

def decode_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, settings.SECRET, algorithms=[settings.ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
