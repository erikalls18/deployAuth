import fastapi
from api.users import router
import psycopg2
from create_data import init_db, get_db_connection


app = app = fastapi.FastAPI()

app.include_router(router)

@app.get("/")
async def check_api():
    return {'msg':"The app is running"}




#command to execute 
 #uvicorn main:app --reload
