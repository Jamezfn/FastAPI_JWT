import jwt
import time
from decouple import config

JWT_SECRET = config("JWT_SECRET")
JWT_ALGORITHMN = config("JWT_ALGORITHMN")

class AuthHandler(object):
    @staticmethod
    def sign_jwt(user_id: int) -> str:
        payload = {
            "user_id": user_id,
            "expire": time.time() + 900
        }

        token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHMN)

        return token
    
    @staticmethod
    def decode_jwt(token: str) -> dict:
        try:
            decode_token = jwt.decode(token, JWT_SECRET, algorithms=JWT_ALGORITHMN)
            return decode_token if decode_token["expire"] >= time.time() else None
        except:
            print("unable to decode token")
            return None