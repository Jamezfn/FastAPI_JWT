from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.db.schema.user import UserIncreate, UserInlogin, UserWithToken, UserOutput
from app.service.user import UserService

router = APIRouter()

@router.post("/login", status_code=status.HTTP_200_OK, response_model=UserWithToken)
def login(loginDetails: UserInlogin, session: Session = Depends(get_db)):
    return UserService(session=session).login(loginDetails=loginDetails)

@router.post("/signup", status_code=status.HTTP_201_CREATED, response_model=UserOutput)
def sign_Up(signUpDetails: UserIncreate, session: Session = Depends(get_db)):
    return UserService(session=session).signup(user_details=signUpDetails)

