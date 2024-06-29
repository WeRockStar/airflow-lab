# Trigger Other DAGs

## 1. Create a new DAGs

Create a `trigger_me.py` file in the `dags` folder

## 2. Modify `github_to_postgres.py`

- Append `TriggerDagRunOperator` at the last of operator
- Revise relation between operators

```python {"id":"01HYPZRSMWQ072TJ6JEG5B1MY1"}
from airflow.operators.dagrun_operator import TriggerDagRunOperator

...


    trigger = TriggerDagRunOperator(
        task_id='trigger_next_dag',
        trigger_dag_id='trigger_me',
        conf={"message": "อรุณเบิกฟ้า"},
    )

    extract_user >> create_user_table >> insert_user >> trigger

```

### 3. Write the `trigger_me.py` file

```python {"id":"01HYPZRSMWQ072TJ6JEJ7PSEA3"}
from airflow import DAG
from datetime import datetime

from airflow.operators.bash import BashOperator


with DAG('trigger_me', start_date=datetime(2024, 5, 1),
         catchup=False) as dag:

    sing_song = BashOperator(
        task_id='hello_world',
        bash_command='echo "$message นกกาโบยบิน"',
        env={'message': '{{ dag_run.conf["message"] }}'}
    )

    sing_song

```

[Back to Root](../../README.md)
[Go Next](../chapter-10/README.md)
