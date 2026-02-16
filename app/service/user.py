from app.db.repository.user import UserRepository
from app.db.schema.user import UserIncreate, UserOutput, UserInlogin, UserWithToken
from app.core.security.authHandler import AuthHandler
from app.core.security.hashHandler import HashHelper

from sqlalchemy.orm import Session
from fastapi import HTTPException, status

class UserService:
    def __init__(self, session: Session):
        self.__userRepository = UserRepository(session=session)

    def signup(self, user_details: UserIncreate):
        if self.__userRepository.user_exist_by_email(email=user_details.email):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Please Login")
        
        hashed_password = HashHelper.get_hashed_password(plain_password=user_details.password)
        user_details.password = hashed_password
        return self.__userRepository.create_user(user_data=user_details)
    

    def login(self, loginDetails: UserInlogin) -> UserWithToken:
        if not self.__userRepository.user_exist_by_email(email=loginDetails.email):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Please create an account")
        
        user = self.__userRepository.get_user_by_email(email=loginDetails.password)
        if HashHelper.verify_password(plain_password=loginDetails.password, hashed_password=user.password):
            token = AuthHandler.sign_jwt(user_id=user.id)
            if token:
                return UserWithToken(token=token)
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Unable to process request")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Please check your credentials")