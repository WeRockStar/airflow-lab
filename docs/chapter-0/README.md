# Configurations

## Lightweight Airflow on Local

- `CeleryExecutor` to `LocalExecutor`
- Disable Celery related configurations
  - `redis`
  - `flower`
  - `airflow-triggerer`
  - `AIRFLOW__CELERY__RESULT_BACKEND`
  - `AIRFLOW__CELERY__BROKER_URL`

## Enable Test Connection

Enable the `AIRFLOW__CORE__TEST_CONNECTION` environment variable to allow the `Test Connection` button to appear in the Airflow UI.

`AIRFLOW__CORE__TEST_CONNECTION: Enabled`