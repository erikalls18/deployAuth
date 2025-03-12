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



