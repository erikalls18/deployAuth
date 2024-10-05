import jwt
from fastapi import HTTPException, Security

from fastapi.security import HTTPAuthorizationCredentials , HTTPBearer

from pydantic_schemas.squema_users import Users, LoginUser
from api.utils.controller_users import get_user
from api.utils.auth import Auth
import fastapi
from typing import List



router = fastapi.APIRouter()
users = []
auth= Auth()

import fastapi

@router.get("/users", response_model= List[ Users])
async def get_users():
    return 


@router.post("/login")
async def get_auth_user(login_user: LoginUser):
    user = auth.authenticate_user(login_user)
    if not user:
        raise fastapi.HTTPException(status_code=401, detail="Invalid credentials")
    return user

    '''fetched_user= get_user(user.email, user.password)
    if fetched_user:
        return {"message": "User authenticated successfully", "user": fetched_user}
    else:
        return {"message": "Invalid email or password"},'''
