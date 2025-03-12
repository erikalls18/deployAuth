import fastapi
from routes.user_route import router

app = app = fastapi.FastAPI()

app.include_router(router)

@app.get("/")
async def check_api():
    return {'msg':"The app is running"}



