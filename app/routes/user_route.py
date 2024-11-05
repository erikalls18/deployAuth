import jwt
from fastapi.security import HTTPAuthorizationCredentials , HTTPBearer
from db.pydantic_schemas.squema_users import Users, LoginUser
from api.utils.controller_users import get_user
from api.utils.auth import Auth , create_access_token
import fastapi




router = fastapi.APIRouter()
users = []
auth= Auth()



@router.post("/login")
async def get_auth_user(login_user: LoginUser):
    user = auth.authenticate_user(login_user)
    if not user:
        raise fastapi.HTTPException(status_code=401, detail="Invalid credentials")
    #return user
    access_token = create_access_token(data={"sub": user[1]})  #access token base on email
    return {"access_token": access_token, "token_type": "bearer"}

