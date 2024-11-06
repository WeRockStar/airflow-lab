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

Start DataHub via `datahub` CLI:

```bash
datahub docker quickstart -f docker-compose-datahub.yaml
# ☕️ take time to start and see the output below
```

Console output:

```bash
[+] Running 12/12
 ✔ Container datahub-zookeeper-1               Healthy                                                                                  0.5s
 ✔ Container datahub-mysql-1                   Healthy                                                                                  0.5s
 ✔ Container datahub-broker-1                  Healthy                                                                                  1.6s
 ✔ Container datahub-mysql-setup-1             Exited                                                                                   6.6s
 ✔ Container datahub-schema-registry-1         Healthy                                                                                  1.5s
 ✔ Container datahub-elasticsearch-1           Healthy                                                                                  0.5s
 ✔ Container datahub-kafka-setup-1             Exited                                                                                   4.5s
 ✔ Container datahub-elasticsearch-setup-1     Exited                                                                                   4.9s
 ✔ Container datahub-datahub-upgrade-1         Exited                                                                                  28.7s
 ✔ Container datahub-datahub-gms-1             Healthy                                                                                 29.2s
 ✔ Container datahub-datahub-frontend-react-1  Started                                                                                  0.6s
 ✔ Container datahub-datahub-actions-1         Started                                                                                  0.6s
............
✔ DataHub is now running
Ingest some demo data using `datahub docker ingest-sample-data`,
or head to http://localhost:9002 (username: datahub, password: datahub) to play around with the frontend.
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
