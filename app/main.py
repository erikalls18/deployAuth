import fastapi
from api.endpoint_users import router




app = app = fastapi.FastAPI()

app.include_router(router)

@app.get("/")
async def check_api():
    return {'msg':"The app is running"}




#command to execute 
 #uvicorn main:app --reload
