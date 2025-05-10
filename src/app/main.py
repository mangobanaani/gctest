# src/app/main.py
from fastapi import FastAPI

# Create a FastAPI application instance
app = FastAPI()

# Define a simple endpoint
@app.get("/")
async def read_root():
    return {"message": "Hello from your Dockerized FastAPI app!"}


