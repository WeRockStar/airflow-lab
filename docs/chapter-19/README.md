# Airflow Docker Image

## Introduction

In this chapter, we will learn how to build an Airflow Docker image using Poetry for package management. We will use the official Airflow Docker image as the base image and install the required dependencies using Poetry.

## Prerequisites

- `Docker Desktop` installed on your machine
- `Dockerfile` at the root of the project

## Build Airflow Docker Image

```bash
docker build -t airflow-poetry:2.10.3 .
```

## Let's Try

1. Look at `.env` file and update the `AIRFLOW_IMAGE_NAME`

   Currently, it is set to `apache/airflow:2.10.3`, you can change it to `airflow-poetry:2.10.3`.

   ```bash
   AIRFLOW_IMAGE_NAME=apache/airflow:2.10.3
   AIRFLOW_UID=50000
   ```

   Change it to and ensure environment variables are set correctly. Run `source .env` to set the environment variables.

   ```bash
   AIRFLOW_IMAGE_NAME=airflow-poetry:2.10.3
   AIRFLOW_UID=50000
   ```

2. Run the Airflow Docker image

   ```bash
   docker-compose -f docker-compose.lite.yaml up
   ```
