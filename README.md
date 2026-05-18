# Data Platform Project

## Overview

End-to-end modern data platform built with:

- Airflow
- Kafka
- Spark
- Feast
- Grafana
- ClickHouse
- MinIO
- Great Expectations
- Docker
- Terraform

---

# Architecture

## Ingestion
- CSV files
- Kafka streaming events

## Processing
- Pandas transformations
- Spark processing

## Storage
- Bronze / Silver / Gold Lakehouse
- MinIO object storage

## Orchestration
- Apache Airflow

## Streaming
- Kafka Producer / Consumer

## Feature Store
- Feast

## Monitoring
- Grafana + ClickHouse

## Infrastructure
- Docker Compose
- Terraform

---

# Project Structure

```text
bronze/
silver/
gold/
dags/
feature_repo/
data/