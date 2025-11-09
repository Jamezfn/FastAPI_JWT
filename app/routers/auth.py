from fastapi import APIRouter, Response, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends

from schemas.auth import UserCreate
from db_utils.dB import get_db
from db_utils.user import create, get

router = APIRouter(
    prefix='/auth',
    tags=['auth'],
    responses={404: {"description": "Not found"}}
)

@router.get('/')
def index():
    return  Response(status_code=status.HTTP_200_OK, content="Welcome to the Auth API")

@router.post('/register')
def register(request: UserCreate, db: Session = Depends(get_db)):
    return create(request, db)

@router.post('/login')
def login(request: UserCreate, db: Session = Depends(get_db)):
    return get(request, db)

@router.get('/logout')
def logout():
    return Response(status_code=status.HTTP_200_OK, content="Logout endpoint")