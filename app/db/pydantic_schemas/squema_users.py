from pydantic import BaseModel


class Users(BaseModel): 
    user_id: int
    username: str
    password: str
    email: str
    rol:str
  

class LoginUser(BaseModel):
    email:str
    password:str



SECRET_KEY = "fd78e4a483e426dee527b1f85686628fa15cc23a05786164d8f6ffa38692cf56"