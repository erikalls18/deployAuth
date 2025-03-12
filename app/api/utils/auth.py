from passlib.context import CryptContext
from db.pydantic_schemas.squema_users import LoginUser
from api.utils.controller_users import get_user
from fastapi import Depends,  HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta, timezone
import jwt
from typing import Optional
from pydantic import BaseModel

from jwt.exceptions import InvalidTokenError
import os


SECRET_KEY= os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')



class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
     username: Optional[str] = None 


ACCESS_TOKEN_EXPIRE_MINUTES = 30
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

       

class Auth(): 

    def __init__(self):

        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


    def verify_password(self, plain_password, hashed_password):

        return self.pwd_context.verify(plain_password, hashed_password)

    def authenticate_user(self, user: LoginUser):
        fetched_user= get_user(user.email)
        if not fetched_user:
            return False

        if not self.verify_password(user.password, fetched_user[2]):
            return False
        return fetched_user
    

#data: data inluded in token 
#to_encode is created a copy from data to avoid alter the original data
def create_access_token( data: dict,  expires_delta: Optional[timedelta] = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.now(timezone.utc) + expires_delta
        else:
            expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
      
      
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY.encode(), algorithm=ALGORITHM)
        try:
            decoded = jwt.decode(encoded_jwt, SECRET_KEY, algorithms=[ALGORITHM])
            print("Invalid Token. Content:", decoded)
            expiration_time = decoded["exp"]
            current_time = datetime.now(timezone.utc).timestamp() 
            print(expiration_time)
        except Exception as e:
            print("Error decoding the token:", e)


   
       
        return encoded_jwt

