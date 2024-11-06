# Working with DataHub

## Introduction

DataHub is a data platform that provides a unified view of data across an organization. It is designed to be a central place for **data discovery, collaboration, and governance**. DataHub is built on top of a graph database and provides a rich set of features for managing metadata, lineage, and data quality.

## Start Airflow

Note: Ensure Airflow image is build from `Dockerfile`. see [chapter-18](./../chapter-18/README.md) for more details.

```bash
docker-compose -f docker-compose.lite.yaml up
```

## Start DataHub on Local

Ensure you're in virtual environment:

```bash
poetry shell
```

Start DataHub using Docker Compose:

```bash
datahub docker quickstart -f docker-compose-datahub.yaml
```

## DataHub Plugin

I have added a DataHub plugin to Airflow. Look at `pyproject.toml` file to see the dependencies.

```toml
[tool.poetry.dependencies]
...
acryl-datahub-airflow-plugin = "^0.14.1.6"
```

## Create DataHub Connection

```bash
airflow connections add  --conn-type 'datahub-rest' 'datahub_rest_default' --conn-host 'http://datahub-gms:8080'
```
