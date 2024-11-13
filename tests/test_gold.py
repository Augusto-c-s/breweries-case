import os
import pandas as pd
from src.data.gold_layer import gold_layer
from src.data.silver_layer import silver_layer
from src.data.bronze_layer import bronze_layer

def test_create_gold_layer():
    test_data = [
        {"id": "1", "name": "Brewery Test", "state": "CA", "brewery_type": "micro", "city": "Los Angeles", "country": "US"},
        {"id": "2", "name": "Brewery Test 2", "state": "CA", "brewery_type": "micro", "city": "San Francisco", "country": "US"},
        {"id": "3", "name": "Brewery Test 3", "state": "NY", "brewery_type": "brewpub", "city": "New York", "country": "US"}
    ]
   
    bronze_layer(test_data)
    silver_layer()
    gold_layer()
    
    assert os.path.exists("app/data_lake/gold/breweries_aggregated.parquet")
    
    df = pd.read_parquet("app/data_lake/gold/breweries_aggregated.parquet")
    assert len(df) > 0
    assert "brewery_count" in df.columns
