from fastapi import APIRouter
from src.utils.api_client import fetch_breweries_data
from src.data.bronze_layer import bronze_layer
from src.data.silver_layer import silver_layer
from src.data.gold_layer import gold_layer

router = APIRouter()

@router.get("/get_breweries")
def get_breweries():
    data = fetch_breweries_data()
    return {"status": "Success", "Data": data}

@router.post("/bronze_layer")
def bronze():
    data = fetch_breweries_data()
    bronze_layer(data)
    return {"message": "Data saved to Bronze layer"}

@router.post("/silver_layer")
def silver():
    silver_layer()
    return {"message": "Data saved to Silver layer"}

@router.post("/gold_layer")
def gold():
    gold_layer()
    return {"message": "Data saved to Gold layer"}