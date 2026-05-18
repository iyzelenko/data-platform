# Data Platform Project

## Overview

Современная end-to-end Data Platform для обработки batch и streaming данных.

Проект демонстрирует построение полного data engineering pipeline:
- ingestion данных
- ETL orchestration
- streaming processing
- data validation
- feature store
- monitoring
- lakehouse architecture
- infrastructure as code

---

# Technology Stack

| Component | Technology |
|---|---|
| Orchestration | Apache Airflow |
| Streaming | Apache Kafka |
| Processing | Pandas / PySpark |
| Storage | MinIO |
| Lakehouse | Bronze / Silver / Gold |
| Validation | Great Expectations |
| Feature Store | Feast |
| Monitoring | Grafana + ClickHouse |
| Infrastructure | Docker + Terraform |
| CI/CD | GitHub Actions |

---

# Architecture

## Data Sources
- CSV files
- Streaming Kafka events

## Data Ingestion
Apache Airflow orchestrates ETL pipelines and schedules workflows.

## Processing Layer
- Pandas transformations
- Spark processing jobs
- Streaming consumer processing

## Storage Layer
Lakehouse architecture:
- Bronze layer
- Silver layer
- Gold layer

## Feature Engineering
Feast Feature Store stores ML-ready features.

## Monitoring
Grafana dashboards connected to ClickHouse.

---

# Project Structure

```text
dags/                  Airflow DAGs
data/                  Source data
bronze/                Raw layer
silver/                Cleaned layer
gold/                  Aggregated layer
feature_repo/          Feast feature store
producer.py            Kafka producer
consumer.py            Kafka consumer
validate.py            Great Expectations validation
spark_job.py           Spark transformations
main.tf                Terraform IaC
docker-compose.yml     Infrastructure services
Running The Project
Start infrastructure
docker compose up -d
Run validation
python validate.py
Run Kafka producer
python producer.py
Run Kafka consumer
python consumer.py
Features
ETL orchestration
Streaming pipeline
Lakehouse architecture
Data quality validation
Feature store
Monitoring dashboards
Infrastructure as Code
Containerized deployment
Future Improvements
Kubernetes deployment
Real cloud storage
ML model serving
Advanced Grafana dashboards
dbt transformations
Author

Irina Zelenko