# Airflow Testing

## DAG Integrity Testing

From the **Data Pipelines with Apache Airflow** book:

A test verifies all your DAGs for their integrity (i.e., the correctness of the DAG, for example, validating if the DAGs do not contain cycles; if the task IDs in the DAG are unique, etc.)

Create a `dag_integrity_cycle.py` file:

`start >> t1 >> t2 >> end >> t2`

**end >> t2** creates a cycle in the DAG

```python
from airflow import DAG
import datetime
from airflow.operators.empty import EmptyOperator

with DAG(
    dag_id="dag_integrity_cycle",
    start_date=datetime.datetime(2022, 1, 1),
    catchup=False,
    schedule="@daily",
) as dag:
    start = EmptyOperator(task_id="start")

    t1 = EmptyOperator(task_id="t1")

    t2 = EmptyOperator(task_id="t2")

    end = EmptyOperator(task_id="end")

    start >> t1 >> t2 >> end >> t2
```

Create a `tests/dags/test_dag_integrity.py` file:

```python

"""Test integrity of DAGs."""

import glob
import importlib.util
import os

import pytest
from airflow.models import DAG
from airflow.utils.dag_cycle_tester import check_cycle

DAG_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "dags/**.py")
DAG_FILES = glob.glob(DAG_PATH)


@pytest.mark.parametrize("dag_file", DAG_FILES)
def test_dag_integrity(dag_file):
    """Import DAG files and check for DAG."""
    module_name, _ = os.path.splitext(dag_file)
    module_path = os.path.join(DAG_PATH, dag_file)
    mod_spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(mod_spec)
    mod_spec.loader.exec_module(module)

    dag_objects = [var for var in vars(module).values() if isinstance(var, DAG)]
    assert dag_objects

    for dag in dag_objects:
        check_cycle(dag)

```

**Note**: Duplicate task id in the DAG, test also fails

## Unit Testing

## Using dag.test() method

`dag.test()` method is used to test the DAGs in Airflow. It is a method of the DAG class.

[Back to Root](../../README.md)
[Go Next](../chapter-12/README.md)
