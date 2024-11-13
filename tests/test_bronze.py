import os
import json
from src.data.bronze_layer import bronze_layer

def test_save_data_to_bronze():
    test_data = [{"id": "1", "name": "Brewery Test"}]
    bronze_layer(test_data)
    
    assert os.path.exists("app/data_lake/bronze/breweries_raw.json")
    
    with open("app/data_lake/bronze/breweries_raw.json", "r") as f:
        data = json.load(f)
    assert data == test_data