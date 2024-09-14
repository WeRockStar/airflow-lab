# Managing Complex Tasks with TaskGroup

## 1. TaskGroup

In Airflow, you can group tasks together using the `TaskGroup` class. This allows you to manage complex tasks more easily.

### Example

Create a new DAG file `task_group.py`:

```python
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator

from airflow.utils.task_group import TaskGroup
from datetime import datetime

with DAG(
    dag_id='task_group',
    start_date=datetime(2024, 5, 10),
    schedule_interval="@daily",
    catchup=False
) as dag:

    def _task1():
        print('Hello, Task 1')

    def _task2():
        print('Hello, Task 2')

    def _task3():
        print('Hello, Task 3')

    with TaskGroup(group_id='tasks') as tasks:
        task1 = PythonOperator(
            task_id='task1',
            python_callable=_task1
        )

        task2 = PythonOperator(
            task_id='task2',
            python_callable=_task2
        )

        task3 = PythonOperator(
            task_id='task3',
            python_callable=_task3
        )

    start = DummyOperator(task_id='start')
    end = DummyOperator(task_id='end')

    start >> tasks >> end
```

[Back to Root](../../README.md)
[Go Next](../chapter-16/README.md)
