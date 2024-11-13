import os
import pandas as pd
from src.data.silver_layer import silver_layer
from src.data.bronze_layer import bronze_layer

def test_transform_data_to_silver():
    test_data = [{"id": "1", "name": "Brewery Test", "state": "CA", "brewery_type": "micro", "city": "Los Angeles", "country": "US"}]
    
    bronze_layer(test_data)
    silver_layer()
    
    assert os.path.exists("app/data_lake/silver/breweries.parquet")
    
    df = pd.read_parquet("app/data_lake/silver/breweries.parquet")
    assert len(df) > 0
    assert "state" in df.columns
