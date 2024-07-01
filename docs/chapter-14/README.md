# Dependencies between Tasks

## 1. Basic Dependencies

In Airflow, you can define dependencies between tasks using the `>>` operator.

In the following example, we have two tasks, `task1` and `task2`. We want `task2` to run after `task1` has completed (success). To do this, we use the `>>` operator to define the dependency between the two tasks.

```mermaid
graph LR
    task1 --> task2
```

```python
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime


with DAG(
        dag_id='basic_dependencies',
        start_date=datetime(2024, 5, 10),
        schedule_interval="@daily",
        catchup=False
    ) as dag:

    def _task1():
        print('Hello, Task 1')

    def _task2():
        print('Hello, Task 2')

    task1 = PythonOperator(
        task_id='task1',
        python_callable=_task1
    )

    task2 = PythonOperator(
        task_id='task2',
        python_callable=_task2
    )

    task1 >> task2
```

## 2. Fan-in and Fan-out

In Airflow, you can define multiple dependencies between tasks. This is known as fan-in and fan-out.

In the following example, we have three tasks, `task1`, `task2`, and `task3`. We want `task2` and `task3` to run after `task1` has completed (success). To do this, we use the `>>` operator to define the dependencies between the tasks.

### Fan-out

```mermaid
graph LR
    task1 --> task2
    task1 --> task3
```

```python
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

with DAG(
        dag_id='fan_out',
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

    task1 >> [task2, task3]
```

### Fan-in

```mermaid
graph LR
    taskDB --> taskCombineSource
    taskAPI --> taskCombineSource
```

```python
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

with DAG(
    dag_id='fan_in',
    start_date=datetime(2024, 5, 10),
    schedule_interval="@daily",
    catchup=False
) as dag:

    def _taskDB():
        print('Hello, DB')
    def _taskAPI():
        print('Hello, API')
    def _taskCombine():
        print('Hello, Combined Source')
    taskDB = PythonOperator(
        task_id='task1',
        python_callable=_taskDB
    )
    taskAPI = PythonOperator(
        task_id='task2',
        python_callable=_taskAPI
    )
    taskCombineSource = PythonOperator(
        task_id='task3',
        python_callable=_taskCombine
    )
    [taskDB, taskAPI] >> taskCombineSource
```

## 3. Trigger Rules

In Airflow, you can define trigger rules to control when a task is triggered. The default trigger rule is `all_success`, which means that the task is triggered when all upstream tasks have completed successfully.

Here are some of the trigger rules [available in Airflow](https://airflow.apache.org/docs/apache-airflow/1.10.9/concepts.html#trigger-rules):

- `all_success`: (default) all parents have succeeded
- `all_failed`: all parents are in a failed or upstream_failed state
- `all_done`: all parents are done with their execution
- `one_failed`: fires as soon as at least one parent has failed, it does not wait for all parents to be done
- `one_success`: fires as soon as at least one parent succeeds, it does not wait for all parents to be done
- `none_failed`: all parents have not failed (failed or upstream_failed) i.e. all parents have succeeded or been skipped

none_skipped: no parent is in a skipped state, i.e. all parents are in a success, failed, or upstream_failed state

dummy: dependencies are just for show, trigger at will

## 4. Conditional Trigger
