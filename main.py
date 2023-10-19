import uvicorn
from typing import Optional
from fastapi import FastAPI, Request
from pydantic import BaseModel, HttpUrl, EmailStr

app = FastAPI()

class User(BaseModel):
    name: str
    password: str
    avatar_url: Optional[HttpUrl] = None
    
@app.post("/users")
def create_user(user: User):
    return user

@app.get("/")
def hello():
    text = "Hello, World! Change"
    return text

@app.get("/users/me")
def get_user_me():
    return {"user_id" : 123}

@app.get("/users/{user_id}")
def get_user(user_id:int, request: Request):
    print(request.path_params)
    return {"user_id" : user_id}


@app.get("/users")
def get_users(is_admin: bool, limit: int = 100):
    """
    pydantic이 (True, False), (true, false), (1, 0), (yes, no)을 알아서 판단 후 bool을 처리
    """
    return {"is_admin":is_admin, "limit":limit}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
    
