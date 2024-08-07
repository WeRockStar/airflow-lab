# Write Second DAGs with Multiple Operators

In this chapter, you will learn how to create your second DAGs with multiple operators.

## 1. Create a new DAG

Create a `second_dag.py` file in the `dags` folder

## 2. Copy the code from the first DAGs

`catchup=False` is used to prevent backfilling of the DAGs.

```python
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

# Change first_dag to second_dag
with DAG(dag_id='first_dag', start_date=datetime(2024, 5, 10), catchup=False) as dag:

    def print_hello():
        print('Hello, DAGs')

    run_this = PythonOperator(
        task_id='print_hello',
        python_callable=print_hello
    )
```

## 3. Edit DAGs ID

Replace `dag_id='first_dag'` with `dag_id='second_dag'`

```python {"id":"01HYCH15TDF6P9S5JE1Z2WXKA6"}
with DAG(dag_id='second_dag', start_date=datetime(2024, 5, 10), catchup=False) as dag:
```

## 4. Add more operators

Note: Run and See Graph View

```python {"id":"01HYCH15TDF6P9S5JE1Z6T32Z6"}
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

with DAG(dag_id='second_dag', start_date=datetime(2024, 5, 10), catchup=False) as dag:

    def print_hello():
        print('Hello, DAGs')

    run_this = PythonOperator(
        task_id='print_hello',
        python_callable=print_hello
    )

    run_again = PythonOperator(
        task_id='print_hello_again',
        python_callable=print_hello
    )
```

## 5. Define Relationships

Apply this code to define the relationship between the operators.

```python
run_this >> run_again
```

Note: You can define the relationship between the operators using `<<` or `>>` operators, but keep it consistent is a key.

## 6. How Operators and Task Different?

**Operators** are classes that are used to define the task. **Task** is an instance of an operator. By the way, in term of user perspective, they are the same, but in Airflow, they are different.

## 7. Add more operators

Note: Refresh and look at the Graph View

```python
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

with DAG(dag_id='second_dag', start_date=datetime(2024, 5, 10), catchup=False) as dag:

    def print_hello():
        print('Hello, DAGs')

    run_this = PythonOperator(
        task_id='print_hello',
        python_callable=print_hello
    )

    run_again = PythonOperator(
        task_id='print_hello_again',
        python_callable=print_hello
    )

    check_me = PythonOperator(
        task_id='check_me',
        python_callable=print_hello
    )

    run_me = PythonOperator(
        task_id='run_me',
        python_callable=print_hello
    )

    run_me_too = PythonOperator(
        task_id='run_me_too',
        python_callable=print_hello
    )

    run_this >> run_again >> check_me
    check_me >> run_me
    check_me >> run_me_too
```

## 8. Optional - Add more operators

Note: Refresh and See Graph View

```python {"id":"01HYFEMKQ5RYDEYP5X7JHY88PH"}
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

with DAG(dag_id='second_dag', start_date=datetime(2024, 5, 10), catchup=False) as dag:

    def print_hello():
        print('Hello, DAGs')

    run_this = PythonOperator(
        task_id='print_hello',
        python_callable=print_hello
    )

    run_again = PythonOperator(
        task_id='print_hello_again',
        python_callable=print_hello
    )

    check_me = PythonOperator(
        task_id='check_me',
        python_callable=print_hello
    )

    run_me = PythonOperator(
        task_id='run_me',
        python_callable=print_hello
    )

    run_me_too = PythonOperator(
        task_id='run_me_too',
        python_callable=print_hello
    )

    stop_here = PythonOperator(
        task_id='stop_here',
        python_callable=print_hello
    )

    run_this >> run_again >> check_me
    check_me >> run_me >> stop_here
    check_me >> run_me_too >> stop_here
```

[Back to Root](../../README.md)
[Go Next](../chapter-05/README.md)
