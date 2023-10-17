import uvicorn
from fastapi import FastAPI, Request

app = FastAPI()

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



if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
    
