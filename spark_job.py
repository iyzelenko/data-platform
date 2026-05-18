import pandas as pd
import os

# Создание папок
os.makedirs("bronze/students", exist_ok=True)
os.makedirs("silver/students", exist_ok=True)
os.makedirs("gold/avg_grade", exist_ok=True)

# Чтение parquet
df = pd.read_parquet("data/students.parquet")

# Bronze
df.to_parquet(
    "bronze/students/data.parquet",
    index=False
)

# Silver
clean_df = df.drop_duplicates()

clean_df.to_parquet(
    "silver/students/data.parquet",
    index=False
)

# Gold
gold_df = pd.DataFrame({
    "avg_grade": [clean_df["grade"].mean()]
})

gold_df.to_parquet(
    "gold/avg_grade/data.parquet",
    index=False
)

print("Bronze Silver Gold created successfully")