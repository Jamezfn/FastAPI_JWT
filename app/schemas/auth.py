from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str

class UserUpdate(BaseModel):
    username: str | None = None
    password: str | None = None

class UserResponse(BaseModel):
    id: int
    username: str
    is_active: bool

class UserLogin(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    expires_in: int