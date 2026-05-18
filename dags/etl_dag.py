from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd

def etl():
    df = pd.read_csv('/opt/airflow/data/students.csv')
    df.to_parquet('/workspaces/data-platform/data/students.parquet')

with DAG(
    dag_id='etl_pipeline',
    start_date=datetime(2024, 1, 1),
    schedule_interval='@daily',
    catchup=False
) as dag:

    task = PythonOperator(
        task_id='run_etl',
        python_callable=etl
    )