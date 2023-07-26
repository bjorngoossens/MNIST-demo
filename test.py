import pandas as pd

df_towing_vehicles = pd.read_parquet("../test-data/data/towing_vehicles.parquet")
print(df_towing_vehicles.head())
