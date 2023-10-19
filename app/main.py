from typing import List, IO
from fastapi import Depends, FastAPI, HTTPException, Form, File, UploadFile
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from tempfile import NamedTemporaryFile

from . import models, schemas
from .database import SessionLocal, engine

import uvicorn

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@app.post("/users", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session=Depends(get_db)):
    existed_user = db.query(models.User).filter_by(
        email = user.email
    ).first()
    
    if existed_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    user = models.User(email=user.email, password=user.password)
    db.add(user)
    db.commit()
    
    return user

@app.post("/login")
def login(username:str=Form(...), password: str=Form(...)):
    return {"username": username}

@app.post("/file/size")
def get_filesize(file: bytes = File(...)):
    return {"file_size": len(file)}

@app.post("/file/info")
def get_file_info(file: UploadFile = File(...)):
    return {
        "content_type": file.content_type,
        "file_name": file.filename
    }

@app.get("/users", response_model=List[schemas.User])
def read_users(db: Session=Depends(get_db)):
    return db.query(models.User).all()