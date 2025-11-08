from fastapi import APIRouter, Response, status

router = APIRouter(
    prefix='/auth',
    tags=['auth'],
    responses={404: {"description": "Not found"}}
)

@router.get('/')
def index():
    return  Response(status_code=status.HTTP_200_OK, content="Welcome to the Auth API")