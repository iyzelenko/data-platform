# Data Platform Project

## Overview

Современная end-to-end Data Platform для обработки batch и streaming данных.

Проект демонстрирует построение полного data engineering pipeline:
- ingestion данных
- ETL orchestration
- streaming processing
- data validation
- monitoring
- lakehouse architecture
- semantic layer
- infrastructure as code

---

# Technology Stack

| Component | Technology |
|---|---|
| Orchestration | Apache Airflow |
| Streaming | Apache Kafka |
| Processing | Pandas / PySpark |
| Storage | MinIO |
| OLAP Database | ClickHouse |
| Lakehouse | Bronze / Silver / Gold |
| Validation | Great Expectations |
| Monitoring | Grafana |
| Dashboard | Streamlit |
| Semantic Layer | Cube.js |
| Infrastructure | Docker |
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
- Bronze layer — raw data
- Silver layer — cleaned data
- Gold layer — aggregated analytics

## Monitoring Layer
Grafana dashboards connected to ClickHouse for analytics and monitoring.

## Dashboard Layer
Interactive Streamlit dashboards for analytics visualization.

## Semantic Layer
Cube.js provides semantic modeling for analytics queries.

---

# Project Structure

```text
dags/                  Airflow DAGs
data/                  Source data
bronze/                Raw layer
silver/                Cleaned layer
gold/                  Aggregated layer
cube/schema/           Cube.js semantic models
tests/                 Unit tests
.github/workflows/    CI/CD pipelines

producer.py            Kafka producer
consumer.py            Kafka consumer
validate.py            Great Expectations validation
spark_job.py           Spark transformations
app.py                 Streamlit dashboard
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
Run Streamlit dashboard
streamlit run app.py
Features
ETL orchestration with Airflow
Streaming pipeline with Kafka
Lakehouse architecture
Data quality validation
Telegram failure notifications
Monitoring dashboards
Streamlit analytics dashboard
Cube.js semantic layer
Infrastructure as Code
Containerized deployment
CI/CD with GitHub Actions
Monitoring & Analytics
Grafana
operational dashboards
ClickHouse integration
metrics visualization
Streamlit
interactive analytics dashboard
faculty filtering
average grade analytics
visual charts
CI/CD

GitHub Actions pipeline includes:

automated testing
code validation
deployment workflow preparation
Future Improvements
Kubernetes deployment
Cloud object storage
Advanced Spark jobs
Real-time analytics
dbt transformations
ML model serving
Production monitoring stack
Author

Irina Zelenko