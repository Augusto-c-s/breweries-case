import pandas as pd
import os
from src.core.config import DATA_LAKE_PATH

def gold_layer():
    silver_path = os.path.join(DATA_LAKE_PATH, "silver/breweries.parquet")
    
    df = pd.read_parquet(silver_path)
    df_gold = df.groupby(['brewery_type', 'state'], observed=False).size().reset_index(name='brewery_count')

    
    gold_path = os.path.join(DATA_LAKE_PATH, "gold")
    os.makedirs(gold_path, exist_ok=True)
    
    df_gold.to_parquet(f"{gold_path}/breweries_aggregated.parquet", index=False)
