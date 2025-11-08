from fastapi import APIRouter, Response, status
from sqlalchemy.orm import Session
from schemas.auth import UserCreate
from fastapi import Depends

from db_utils.dB import get_db
from db_utils.user import create

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

@router.get('/login')
def login():
    return Response(status_code=status.HTTP_200_OK, content="Login endpoint")


@router.get('/logout')
def logout():
    return Response(status_code=status.HTTP_200_OK, content="Logout endpoint")