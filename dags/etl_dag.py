from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd

def load_csv_to_parquet():

    df = pd.read_csv('/workspaces/data-platform/data/students.csv')

    df.to_parquet(
        '/workspaces/data-platform/data/students.parquet',
        index=False
    )

    print("Parquet created")

with DAG(
    dag_id='etl_pipeline',
    start_date=datetime(2024,1,1),
    schedule='@hourly',
    catchup=False
) as dag:

    load_task = PythonOperator(
        task_id='load_csv',
        python_callable=load_csv_to_parquet,
        retries=3
    )