# Schedule your DAG

Again, Airflow designed to batch-oreinted processing

## 1. Fixed Interval Schedule

```python {"id":"01HYCQ6TM1PC4C06T3TCJ67CYM"}
from datetime import timedelta

dag = DAG(
    'my_dag',
    default_args=default_args,
    description='A simple DAG',
    schedule_interval=timedelta(days=1),
)
```

## 2. Cron Schedule

For example, '0 0 * * *' would schedule the DAG to run daily at midnight

```python {"id":"01HYCQ6TM1PC4C06T3TEQE3QXF"}
dag = DAG(
    'my_dag',
    default_args=default_args,
    description='A simple DAG',
    schedule_interval='0 0 * * *',
)
```

## 3. Preset Airflow Schedules

Airflow provides some preset schedules you can use with the `schedule_interval` parameter

- `@once`: Run the DAG once and then never again
- `@hourly`: Run the DAG every hour
- `@daily`: Run the DAG every day
- `@weekly`: Run the DAG every week
- `@monthly`: Run the DAG every month
- `@yearly`: Run the DAG every year
- `None`: Don't schedule the DAG, use to trigger it with external triggers or manually run

```python {"id":"01HYCQ6TM1PC4C06T3TEYTTXNG"}
dag = DAG(
    'my_dag',
    default_args=default_args,
    description='A simple DAG',
    schedule_interval='@daily',
)
```

[Back to Root](../../README.md)
[Go to Next](../chapter-06/README.md)