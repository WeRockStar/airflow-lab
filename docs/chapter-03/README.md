# Write Your First DAGs - Single Operator

## 1. Create Python file

Create a `first_dag.py` within the `dags` directory

## 2. Import DAGs

```python {"id":"01HYB78YJZ3S6B5322TAWATSRT"}
from airflow import DAG
```

## 3. Define DAGs
Define and refresh the Airflow UI and you should see the `first_dag` DAG

```python
from airflow import DAG

with DAG(dag_id='first_dag') as dag:
    pass
```

## 4. Define Start Date

```python
from airflow import DAG
from datetime import datetime

with DAG(dag_id='first_dag', start_date=datetime(2024, 5, 10), catchup=False) as dag:
    pass
```

## 5. Add an Operator

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

## 6. Learn How Airflow UI Works
1. Manual Trigger
2. Graph View
3. Log View (Specific Task)
4. Code View
5. Next Run

## 7. Go Back to Catchup Mode

`Catchup` is a parameter that allows you to run all the historical DAG runs that you missed. This is useful when you are backfilling data.

Run and see the difference between `catchup=True` and `catchup=False` - Delete the DAG and re-run the DAG with `catchup=True`

Note: `catchup` is set to `True` by default

```python
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

with DAG(dag_id='first_dag', start_date=datetime(2024, 5, 10), catchup=True) as dag:

    def print_hello():
        print('Hello, DAGs')

    run_this = PythonOperator(
        task_id='print_hello',
        python_callable=print_hello
    )

```