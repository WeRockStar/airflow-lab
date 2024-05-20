# Write Second DAGs with Multiple Operators

## 1. Create a new DAG

Create a `second_dag.py` file in the `dags` folder


## 2. Copy the code from the first DAGs

`catchup=False` is used to prevent backfilling of the DAGs.

```python
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

with DAG(dag_id='first_dag', start_date=datetime(2024, 5, 10), catchup=False) as dag:

    def print_hello():
        print('Hello, DAGs')

    run_this = PythonOperator(
        task_id='print_hello',
        python_callable=print_hello
    )
```

## 3. Edit DAGs ID

```python
with DAG(dag_id='second_dag', start_date=datetime(2024, 5, 10), catchup=False) as dag:
```

## 4. Add more operators

Note: Run and See Graph View

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
```

## 5. Define Relationships

Note: Apply and See Graph View

```python
run_this >> run_again
```