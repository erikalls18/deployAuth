import jwt
from fastapi import HTTPException, Security

from fastapi.security import HTTPAuthorizationCredentials , HTTPBearer
from fastapi import Depends
from db.pydantic_schemas.squema_users import Users, LoginUser
from api.utils.controller_users import get_user
from api.utils.auth import Auth , create_access_token, get_current_user
import fastapi
from typing import List



router = fastapi.APIRouter()
users = []
auth= Auth()



@router.get("/users")
async def get_user(current_user: LoginUser = Depends(get_current_user)):
    return current_user


@router.post("/login")
async def get_auth_user(login_user: LoginUser):
    user = auth.authenticate_user(login_user)
    if not user:
        raise fastapi.HTTPException(status_code=401, detail="Invalid credentials")
    #return user
    access_token = create_access_token(data={"sub": user[1]})  #acces token base on email
    return {"access_token": access_token, "token_type": "bearer"}

