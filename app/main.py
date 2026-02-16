from fastapi import FastAPI
from .database import engine, Base
from . import models

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Kalmy API",
    description="A simple FastAPI application for Kalmy",
    version="0.2.0"
)

@app.get("/")
def root():
    return {"message": "API is running!"}