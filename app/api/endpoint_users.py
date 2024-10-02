from pydantic_schemas.squema_users import Users, LoginUser
from api.utils.controller_users import get_user
import fastapi
from typing import List


router = fastapi.APIRouter()
users = []

import fastapi

@router.get("/users", response_model= List[ Users])
async def get_users():
    return 


@router.post("/login")
async def get_auth_user(user: LoginUser):
    fetched_user= get_user(user.email, user.password)
    if fetched_user:
        return {"message": "User authenticated successfully", "user": fetched_user}
    else:
        return {"message": "Invalid email or password"},
