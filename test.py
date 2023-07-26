import pandas as pd
import os

print("Listing current dir")
print(os.listdir("./"))

print("Listing dir above")
print(os.listdir("./../"))

print("Listing test-data dir")
print(os.listdir("./../test-data"))

df_towing_vehicles = pd.read_parquet("../test-data/data/towing_vehicles.parquet")
print(df_towing_vehicles.head())
