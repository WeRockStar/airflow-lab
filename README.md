# Airflow Lab

## Introduction

This lab is designed to help you get familiar with `Apache Airflow`. You will learn how to create a simple DAG, schedule it, and monitor its execution.

**Note**: You can use `Astro CLI` to create a new Airflow project. For more information, see [Astro CLI](https://www.astronomer.io/docs/astro/cli/get-started-cli)

## Prerequisites

- Basic knowledge of Python
  - Variables
  - Functions
  - Control Flow
  - arg and kwargs
- Basic knowledge of Docker
  - `docker compose up` and `down` is good enough
- poetry: Package Manager for Python
  - `poetry install --no-root` to install dependencies

## Lab Instructions

1. [Configuration](docs/chapter-0/README.md)

   - Lightweight Airflow setup with Docker, see `docker-compose.lite.yaml`
   - Enable Test button in Airflow UI
   - Disable Example DAGs
   - Copy Airflow Configuration
   - Enable **Flower** UI

2. [What's Airflow?](docs/chapter-01/README.md)

   - Workflow Orchestration
   - Data Pipeline

3. [Overview of Airflow UI and concepts](docs/chapter-02/README.md)

   - Airflow UI
     - Pause/Unpause
     - Trigger DAG
     - Refresh
     - Recent Tasks
     - DAG Runs
     - Graph View
   - DAGs
   - Operators
   - Tasks

4. [Writing your first DAG (Single Operator)](docs/chapter-03/README.md)

   - Create a new DAG with `PythonOperator`
   - Defining DAG
     - Schedule
     - Task
   - Test the DAG

5. [Writing your second DAG (Multiple Operators)](docs/chapter-04/README.md)

   - Create a new DAG with `PythonOperator`
   - Define **dependencies** between tasks
   - Test the DAG

6. [Schedule your DAG](docs/chapter-05/README.md)

   - Fixed Interval
   - Cron Expression
   - Preset Airflow Scheduler

7. [Google Drive to GCS](docs/chapter-06/README.md)

   - Create a new DAG
   - Create a new **connection** for Google Drive via Service Account
   - Use `GoogleDriveToGCSOperator` to copy files from Google Drive to GCS
   - Test the DAG

8. [Working with `Sensor`](docs/chapter-07/README.md)

   - `GoogleDriveFileSensor` to wait for a file to be uploaded to Google Drive

9. [Scraping Data from Githubs to Postgres](docs/chapter-08/README.md)

   - `SimpleHTTPOperator` to get data from Github API
   - `PostgresOperator` to insert data into Postgres

10. [Trigger Other DAGs](docs/chapter-09/README.md)

    - Learn how to trigger another DAG
    - Getting to know `TriggerDagRunOperator`

11. [Task Decorators - Taskflow API](docs/chapter-10/README.md)

    - Simplified way to define tasks
    - Getting to know `@task` decorator
    - Using `@task` to define taks like `PythonOperator`

12. [Testing](docs/chapter-11/README.md) - In Progress

    - Unit Testing
    - DAG Integrity Testing
    - `dag.test()` method

13. [Dataset - Data-aware scheduling](docs/chapter-12/README.md) - In Progress

    - Trigger DAG based on the data availability
    - Wait for many datasets to be available

14. [Celery Executor (Local)](docs/chapter-13/README.md)

    - Monitor the task execution with Flower UI (To enable Flower UI, see [chapter-0](docs/chapter-0/README.md))
    - Add more workers to the Celery Executor
      - Duplicate `airflow-worker` service in `docker-compose.yml` and rename it
      - Restart Docker

15. [Dependencies between Tasks](docs/chapter-14/README.md)

    - Basic define dependencies between tasks
    - Fan-in and Fan-out
    - Trigger Rules
    - Conditional Trigger

16. [Managing Complex Tasks with TaskGroup](./docs/chapter-15/README.md) - In Progress
    - Group tasks together
    - Define dependencies between TaskGroups
