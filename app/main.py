from fastapi import FastAPI

app = FastAPI(
    title="Kalmy API",
    description="A simple FastAPI application for Kalmy",
    version="0.1.0"
)

@app.get("/")
def root():
    return {"message": "API is running!"}