import requests
import pandas as pd

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


def etl():
    df = pd.read_csv('/opt/airflow/data/students.csv')

    df.to_parquet(
        '/opt/airflow/data/students.parquet',
        index=False
    )

    raise Exception("TEST ALERT")


def send_telegram_alert(context):
    token = "8928317883:AAGaDhMpa39oiyjUzqjDjX0EbtrapvxkPB8"
    chat_id = "825219417"

    message = f"""
Airflow Alert!

DAG: {context['task_instance'].dag_id}
Task: {context['task_instance'].task_id}
State: FAILED
"""

    url = f"https://api.telegram.org/bot{token}/sendMessage"

    requests.post(
        url,
        json={
            "chat_id": chat_id,
            "text": message
        }
    )


with DAG(
    dag_id='etl_pipeline',
    start_date=datetime(2024, 1, 1),
    schedule='@daily',
    catchup=False
) as dag:

    task = PythonOperator(
        task_id='run_etl',
        python_callable=etl,
        on_failure_callback=send_telegram_alert,
        retries=2
    )