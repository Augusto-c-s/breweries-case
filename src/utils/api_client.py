import requests
from fastapi import HTTPException
from src.core.config import API_URL

def fetch_breweries_data():
    
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        return response.json()
     
    except requests.exceptions.RequestException as error:
        raise HTTPException(status_code=response.status_code, detail=str(error))