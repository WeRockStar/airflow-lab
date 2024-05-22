# Airflow Lab

## Introduction

This lab is designed to help you get familiar with Apache Airflow. You will learn how to create a simple DAG, schedule it, and monitor its execution.

## Prerequisites

- Basic knowledge of Python
- Basic knowledge of Docker

## Lab Instructions

1. [Configuration](docs/chapter-0/README.md)
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
   - Define the schedule
   - Define the tasks
   - Test the DAG

5. [Writing your second DAG (Multiple Operators)](docs/chapter-04/README.md)

   - Create a new DAG with `PythonOperator`
   - Define dependencies between tasks
   - Test the DAG

6. [Schedule your DAG](docs/chapter-05/README.md)

   - Fixed Interval
   - Cron Expression
   - Preset Airflow Scheduler

7. [Google Drive to GCS](docs/chapter-06/README.md)

   - Create a new DAG
   - Create a new connection for Google Drive via Service Account
   - Use `GoogleDriveToGCSOperator` to copy files from Google Drive to GCS
   - Test the DAG

8. [Working with `Sensor`](docs/chapter-07/README.md)

   - `GoogleDriveFileSensor` to wait for a file to be uploaded to Google Drive

9. [Scraping Data from Githubs to Postgres](docs/chapter-08/README.md)

   - `SimpleHTTPOperator` to get data from Github API
   - `PostgresOperator` to insert data into Postgres

10. [Trigger Other DAGs](docs/chapter-09/README.md)

- Trigger a DAG from another DAG