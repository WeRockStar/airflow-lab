from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

with DAG(dag_id="second_dag", start_date=datetime(2024, 5, 10), catchup=False) as dag:

    def print_hello():
        print("Hello, DAGs")

    run_this = PythonOperator(task_id="print_hello", python_callable=print_hello)

    run_again = PythonOperator(task_id="print_hello_again", python_callable=print_hello)

    check_me = PythonOperator(task_id="check_me", python_callable=print_hello)

    run_me = PythonOperator(task_id="run_me", python_callable=print_hello)

    run_me_too = PythonOperator(task_id="run_me_too", python_callable=print_hello)

    stop_here = PythonOperator(task_id="stop_here", python_callable=print_hello)

    run_this >> run_again >> check_me
    check_me >> run_me >> stop_here
    check_me >> run_me_too >> stop_here
