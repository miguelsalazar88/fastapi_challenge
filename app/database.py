import pandas as pd
import pyarrow.parquet as pq
from pathlib import Path

# Global for df
df = None

def load_data():
    global df
    
    data_path = Path("data")

    dataset = pq.ParquetDataset(data_path)

    raw_data = dataset.read().to_pandas()

    df = clean_data(raw_data)


# Some adjustments to data types
def clean_data(raw_data):
    clean_data = raw_data.copy()
    clean_data["KeyDate"] = pd.to_datetime(clean_data['KeyDate'])
    return clean_data

def get_sales_data():
    return df
