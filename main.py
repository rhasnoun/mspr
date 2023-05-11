import os
import uvicorn
from fastapi import FastAPI 
from routers import users, plantes, conseil,garde
from dotenv import load_dotenv
from fastapi_sqlalchemy import DBSessionMiddleware

load_dotenv(".env")

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])
app.include_router(users.router)
app.include_router(plantes.router)
app.include_router(conseil.router)
app.include_router(garde.router)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)