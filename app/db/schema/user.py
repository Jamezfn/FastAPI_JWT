from pydantic import BaseModel, EmailStr
from typing import Union

class UserIncreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str

class UserOutput(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: EmailStr

class UserInUpdate(BaseModel):
    id: str
    first_name: Union[str, None] = None
    last_name: Union[str, None] = None
    email: Union[EmailStr, None] = None
    password: str | None = None

class UserInlogin(BaseModel):
    email: EmailStr
    password: str

class UserWithToken(BaseModel):
    token: str