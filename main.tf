terraform {
  required_providers {
    docker = {
      source = "kreuzwerker/docker"
    }
  }
}

provider "docker" {}

resource "docker_container" "airflow" {
  name  = "airflow"
  image = "apache/airflow:2.8.1-python3.10"
}

resource "docker_container" "kafka" {
  name  = "kafka"
  image = "confluentinc/cp-kafka:7.4.0"
}

resource "docker_container" "grafana" {
  name  = "grafana"
  image = "grafana/grafana"
}