import requests
import pandas as pd

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


# EXTRACT

def extract():

    raw_df = pd.read_csv('/opt/airflow/data/students.csv')

    raw_df.to_parquet(
        '/opt/airflow/bronze/students_raw.parquet',
        index=False
    )

    print("Bronze layer created")


# VALIDATE + TRANSFORM

def validate():

    raw_df = pd.read_parquet(
        '/opt/airflow/bronze/students_raw.parquet'
    )

    clean_df = raw_df.dropna()

    clean_df.to_parquet(
        '/opt/airflow/silver/students_clean.parquet',
        index=False
    )

    gold_df = (
        clean_df[["grade", "attendance"]]
        .mean()
        .to_frame()
        .reset_index()
    )

    gold_df.columns = ["metric", "avg_value"]

    gold_df.to_parquet(
        '/opt/airflow/gold/student_metrics.parquet',
        index=False
    )

    print("Silver and Gold layers created")


# LOAD TO CLICKHOUSE

def load_to_clickhouse():

    df = pd.read_parquet(
        '/opt/airflow/silver/students_clean.parquet'
    )

    create_table_query = """
    CREATE TABLE IF NOT EXISTS student_events (
        student_id UInt32,
        name String,
        grade Float32,
        attendance Float32
    )
    ENGINE = MergeTree()
    ORDER BY student_id
    """

    response = requests.post(
        "http://clickhouse:8123/",
        params={"query": create_table_query}
    )

    print(response.text)

    values = []

    for _, row in df.iterrows():

        values.append(
            f"({row['student_id']}, '{row['name']}', {row['grade']}, {row['attendance']})"
        )

    insert_query = (
        "INSERT INTO student_events VALUES "
        + ",".join(values)
    )

    response = requests.post(
        "http://clickhouse:8123/",
        params={"query": insert_query}
    )

    print(response.text)

    print("Loaded to ClickHouse")


# TELEGRAM ALERT

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


# DAG

with DAG(
    dag_id='etl_pipeline',
    start_date=datetime(2024, 1, 1),
    schedule='@daily',
    catchup=False
) as dag:

    extract_task = PythonOperator(
        task_id='extract',
        python_callable=extract,
        on_failure_callback=send_telegram_alert
    )

    validate_task = PythonOperator(
        task_id='validate',
        python_callable=validate,
        on_failure_callback=send_telegram_alert
    )

    load_task = PythonOperator(
        task_id='load_to_clickhouse',
        python_callable=load_to_clickhouse,
        on_failure_callback=send_telegram_alert
    )

    
