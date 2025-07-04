import pydantic
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Union

app = FastAPI(title="User Management API")

users_db: Dict[str, pydantic.BaseModel] = {}

class User(BaseModel):
    userID: str
    username: str

@app.post("/users/{userID}", status_code=201)
def createUser(userID: str, userInfo: User):
    if userID in users_db:
        raise HTTPException(status_code=409, detail=f"User with id '{userID}' already exist.")
    users_db[userID] = userInfo
    return {"message": f"User '{userID}' created successfully", "user": userInfo.model_dump()}

@app.get("/users/{userID}")
def displayUserByID(userID: str):
    user = users_db.get(userID)

    if user is None:
        raise HTTPException(status_code=404, detail=f"User with ID '{userID}' not found.")
    return {"User": user.model_dump()}

@app.get("/users/")
def displayAllUser():
    all_users_data = {user_id: user.model_dump() for user_id, user in users_db.items()}
    return {"users": all_users_data}

@app.put("/users/{userID}")
def updateUser(userID: str, userInfo: User):
    if userID not in users_db:
        # If user not found, return a 404 Not Found error
        raise HTTPException(status_code=404, detail=f"User with ID '{userID}' not found.")

        # Update the user information
    users_db[userID] = userInfo
    return {"message": f"User '{userID}' updated successfully", "user": userInfo.model_dump()}


@app.delete("/users/{userID}", status_code=204)
def deleteUser(userID: str):
    if userID not in users_db:
        raise HTTPException(status_code=404, detail=f"User with ID '{userID}' not found.")

    del users_db[userID]
    return {"message": f"User with '{userID} deleted successfully"}