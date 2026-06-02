import pandas as pd

df = pd.read_csv("data/raw/01_fund_master.csv")

print("Columns:")
print(df.columns)

print("\nFirst 5 rows:")
print(df.head())