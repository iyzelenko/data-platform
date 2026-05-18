import pandas as pd

df = pd.read_csv('data/students.csv')

df.to_parquet(
    'data/students.parquet',
    index=False
)

print(df)

print("Parquet created successfully")