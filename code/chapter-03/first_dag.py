from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

with DAG(dag_id="first_dag", start_date=datetime(2024, 5, 10), catchup=False) as dag:

    def print_hello():
        print("Hello, DAGs")

    run_this = PythonOperator(task_id="print_hello", python_callable=print_hello)
