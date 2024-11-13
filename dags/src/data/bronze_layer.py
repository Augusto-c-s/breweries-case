import json
import os
from src.core.config import DATA_LAKE_PATH

def bronze_layer(data):
    path = os.path.join(DATA_LAKE_PATH, "bronze")
    os.makedirs(path, exist_ok=True)
        
    with open(f"{path}/breweries_raw.json", "w") as f:
        json.dump(data, f)