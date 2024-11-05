import fastapi
from routes.user_route import router




app = app = fastapi.FastAPI()

app.include_router(router)

@app.get("/")
async def check_api():
    return {'msg':"The app is running"}


#https://laerciosantanna.medium.com/mastering-restful-api-testing-with-pytest-56d22460a9c4

#command to execute 
 #uvicorn main:app --reload
