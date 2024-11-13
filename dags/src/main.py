from fastapi import FastAPI
from src.api import breweries

app = FastAPI()

app.include_router(breweries.router)

@app.get("/")
def read_root():
    return {"message": "Welcome and waiting your process..."}
