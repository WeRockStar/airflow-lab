# Airflow Lab

## Introduction

This lab is designed to help you get familiar with Apache Airflow. You will learn how to create a simple DAG, schedule it, and monitor its execution.

## Prerequisites

- Basic knowledge of Python
- Basic knowledge of Docker

## Getting Started

1. Clone this repository
2. Create `.env` file in the root directory
3. Run `docker-compose up` to start the Airflow web server and scheduler
4. Open `http://localhost:8080` in your browser and use the following credentials to log in:
   - Username: `airflow`
   - Password: `airflow`

## Lab Instructions

1. What's Airflow?
   - Workflow Orchestration
   - Data Orchestration
   - Data Pipeline
2. Overview of Airflow UI and concepts
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
3. Writing your first DAG - Single Task
   - Create a new DAG with `PythonOperator`
   - Define the schedule
   - Define the tasks
   - Test the DAG
4. Writing your second DAG - Multiple Tasks
   - Create a new DAG with `PythonOperator`
   - Define dependencies between tasks
   - Test the DAG
5. Google Drive to GCS
   - Create a new DAG
   - Create a new connection for Google Drive via Service Account
   - Use `GoogleDriveToGCSOperator` to copy files from Google Drive to GCS
   - Test the DAG
6. Working with `Sensor`
   - `GoogleDriveFileSensor` to wait for a file to be uploaded to Google Drive
7. Scraping Data from Githubs to Postgres
   - `SimpleHTTPOperator` to get data from Github API
   - `PostgresOperator` to insert data into Postgres