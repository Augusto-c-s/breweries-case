import pandas as pd
import os
from src.core.config import DATA_LAKE_PATH

def silver_layer():
    path_bronze = os.path.join(DATA_LAKE_PATH, "bronze/breweries_raw.json")
    data = pd.read_json(path_bronze)
    
    silver_path = os.path.join(DATA_LAKE_PATH, "silver")
    os.makedirs(silver_path, exist_ok=True)
    
    data.to_parquet(f"{silver_path}/breweries.parquet", partition_cols=['state'], index=False)
