from fastapi import FastAPI, HTTPException
from database import DatabaseService
from schemas import User  # Ensure this exists
from typing import List

app = FastAPI()
db_service = DatabaseService()

@app.on_event("startup")
def event_startup():
    pass # Initialize the database connection here if needed

@app.on_event("shutdown")
def event():
    db_service.close_connection()

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Capgemini Interview Project API!"}

@app.post("/users", response_model=User)
def create_user(user: User):
    users_collection = db_service.db["users"]
    result = users_collection.insert_one(user.dict())
    user.id = str(result.inserted_id)
    return user

@app.get("/users", response_model=List[User])
def get_users():
    users_collection = db_service.db["users"]
    users = list(users_collection.find())
    for user in users:
        user["id"] = str(user["_id"])
    return users
