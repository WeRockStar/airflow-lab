# Schedule your DAG

Again, Airflow designed to batch-oreinted processing

## 1. Fixed Interval Schedule

```python {"id":"01HYCK0CBJCTZPY8HCS5PV7B43"}
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

```python
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

```python
dag = DAG(
    'my_dag',
    default_args=default_args,
    description='A simple DAG',
    schedule_interval='@daily',
)
```

[Back to Root](../../README.md)