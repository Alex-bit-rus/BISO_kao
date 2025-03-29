from fastapi import FastAPI
from database import database
import crud
from shemas import UserCreate, User

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.post("/users/", response_model=User)
async def create_user(user: UserCreate):
    user_id = await crud.create_user(user)
    return {"id": user_id, **user.dict()}

@app.get("/users/", response_model=list[User])
async def read_users():
    return await crud.get_users()