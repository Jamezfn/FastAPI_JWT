from fastapi import APIRouter

from app.db.schema.user import UserIncreate, UserInlogin

router = APIRouter()

@router.post("/login")
def login(loginDetails: UserInlogin):
    return {
        "data": loginDetails
    }

@router.post("/signup")
def sign_Up(signUpDetails: UserIncreate):
    return {
        "data": signUpDetails
    }