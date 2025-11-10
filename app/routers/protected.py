from fastapi import APIRouter, Depends

from utils.security import Authenticate

router = APIRouter(
    prefix='/protected',    
)

router.get('/')
def protected_endpoint(current_user=Depends(Authenticate.get_current_user)):
    return {"message": "This is a protected endpoint"}