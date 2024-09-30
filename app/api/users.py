from models.model_users import Users, LoginUser
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
    return user  
