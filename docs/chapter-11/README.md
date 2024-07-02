# Task Decorators - Taskflow API

## Taskflow API

`Taskflow API` aims to simplify the process of creating complex workflows in Airflow. It provides a higher-level API to define tasks, xcoms, and dependencies between tasks.

```python
from airflow.decorators import task
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

with DAG(
        dag_id='taskflow_api',
        start_date=datetime(2024, 5, 10),
        schedule_interval="@daily",
        catchup=False
    ) as dag:

    @task()
    def task1():
        print('Hello, Task 1')

    @task()
    def task2():
        print('Hello, Task 2')

    @task()
    def task3():
        print('Hello, Task 3')

    task1 >> task2 >> task3
```

Actually, It's make `PythonOperator` more readable and easier to understand and no need to wrap the task in a function and pass it to the `PythonOperator`.
