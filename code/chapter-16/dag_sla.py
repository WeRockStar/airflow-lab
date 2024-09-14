from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from datetime import timedelta
import time


def sla_callback(dag, task_list, blocking_task_list, slas, blocking_tis):
    print(
        "SLA missed with informations: ",
        {
            "dag": dag,
            "task_list": task_list,
            "blocking_task_list": blocking_task_list,
            "slas": slas,
            "blocking_tis": blocking_tis,
        },
    )


default_args = {
    "sla": timedelta(minutes=1),
    "sla_miss_callback": sla_callback,
}

with DAG(
    dag_id="dag_sla",
    start_date=datetime(2022, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    default_args=default_args,
) as dag:

    start = DummyOperator(task_id="start")

    def _task():
        print("Task is running")
        time.sleep(65)

    task = PythonOperator(
        task_id="task",
        python_callable=_task,
    )

    end = DummyOperator(task_id="end")

    start >> task >> end
