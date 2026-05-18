import pandas as pd

df = pd.read_parquet('data/students.parquet')

assert df['student_id'].duplicated().sum() == 0

assert df['grade'].between(0,100).all()

assert df['attendance'].between(0,100).all()

print("Validation passed successfully")