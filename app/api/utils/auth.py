from passlib.context import CryptContext
from db.pydantic_schemas.squema_users import LoginUser
from api.utils.controller_users import get_user
from fastapi import Depends,  HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta, timezone
import jwt
from typing import Optional

from pydantic import BaseModel
#from typing import Annotated
from jwt.exceptions import InvalidTokenError
import os

SECRET_KEY= os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')
#ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES')


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
     username: Optional[str] = None 

'''SECRET_KEY = "fd78e4a483e426dee527b1f85686628fa15cc23a05786164d8f6ffa38692cf56"
ALGORITHM = "HS256" '''
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
        #print(data)
        if expires_delta:
            expire = datetime.now(timezone.utc) + expires_delta
        else:
            expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

# Dependencia para obtener el usuario actual
async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username = username)
    except jwt.InvalidTokenError:
        raise credentials_exception
    
    auth = Auth()  # Instanciar la clase Auth
    user = auth.authenticate_user(LoginUser(email = token_data.username))  # Ajustar aquí según sea necesario
    if user is None:
      raise credentials_exception
    return user



async def get_current_active_user(
    current_user:LoginUser= Depends(get_current_user),
):
    '''if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")'''
    return current_user