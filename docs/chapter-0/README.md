# Configurations

## Lightweight Airflow on Local

This setup is for local development and testing purposes. It is not recommended for production use.

- Replace `CeleryExecutor` to `LocalExecutor`
- Disable Celery related configurations
  - `redis`
  - `flower`
  - `airflow-triggerer`
  - `AIRFLOW__CELERY__RESULT_BACKEND`
  - `AIRFLOW__CELERY__BROKER_URL`

## Enable Test Connection

By default, test connection will disable to enable that, adding `AIRFLOW__CORE__TEST_CONNECTION` environment variable to allow the `Test Connection` button to appear in the Airflow UI, such as `AIRFLOW__CORE__TEST_CONNECTION: Enabled`.

## Disable Example DAGs

To disable the example DAGs, set `AIRFLOW__CORE__LOAD_EXAMPLES` to `False`.