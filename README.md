# Airflow Lab

## Introduction

This lab is designed to help you get familiar with Apache Airflow. You will learn how to create a simple DAG, schedule it, and monitor its execution.

## Prerequisites

- Basic knowledge of Python
- Basic knowledge of Docker

## Lab Instructions

0. Enable Test Connect - [chapter 0](docs/chapter-0/README.md)
1. What's Airflow? - [chapter 1](docs/chapter-01/README.md)

   - Workflow Orchestration
   - Data Pipeline

2. Overview of Airflow UI and concepts  - [chapter 2](docs/chapter-02/README.md)

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

3. Writing your first DAG (Single Operator) - [chapter 3](docs/chapter-03/README.md)

   - Create a new DAG with `PythonOperator`
   - Define the schedule
   - Define the tasks
   - Test the DAG

4. Writing your second DAG (Multiple Operators) - [chapter 4](docs/chapter-04/README.md)

   - Create a new DAG with `PythonOperator`
   - Define dependencies between tasks
   - Test the DAG

5. Schedule your DAG - [chapter 5](docs/chapter-05/README.md)
   - Fixed Interval
   - Cron Expression
   - Preset Airflow Scheduler
6. Google Drive to GCS - [chapter 6](docs/chapter-06/README.md)

   - Create a new DAG
   - Create a new connection for Google Drive via Service Account
   - Use `GoogleDriveToGCSOperator` to copy files from Google Drive to GCS
   - Test the DAG

7. Working with `Sensor` - [chapter 7](docs/chapter-07/README.md)

   - `GoogleDriveFileSensor` to wait for a file to be uploaded to Google Drive

8. Scraping Data from Githubs to Postgres - [chapter 8](docs/chapter-08/README.md)

   - `SimpleHTTPOperator` to get data from Github API
   - `PostgresOperator` to insert data into Postgres
9. Trigger Other DAGs - [chapter 9](docs/chapter-09/README.md)
   - Trigger a DAG from another DAG