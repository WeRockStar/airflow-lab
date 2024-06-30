# Configurations

## Lightweight Airflow on Local

This setup is for local development and testing purposes. It is not recommended for production use.

- Replace `CeleryExecutor` to `LocalExecutor`
- Remove **Celery** related configurations
  - `redis`
  - `flower`
  - `airflow-triggerer`
  - `airflow-worker`
  - `AIRFLOW__CELERY__RESULT_BACKEND`
  - `AIRFLOW__CELERY__BROKER_URL`
  - see `docker-compose.lite.yaml` for the result

## Enable Test Connection

By default, test connection will disable to enable that, adding `AIRFLOW__CORE__TEST_CONNECTION` environment variable to allow the `Test Connection` button to appear in the Airflow UI, such as `AIRFLOW__CORE__TEST_CONNECTION: Enabled`.

## Disable Example DAGs

To disable the example DAGs, set `AIRFLOW__CORE__LOAD_EXAMPLES` to `False`.

## Copy airflow.cfg

Copy the `airflow.cfg` file from the container to the host machine.

```bash
docker cp <container_namme>:/opt/airflow/airflow.cfg .
```

## Start Flower UI

Flower is a web-based tool for monitoring and administrating Celery clusters. To start the Flower UI, run the following command:

```bash
docker-compose --profile flower up

# Or try this
docker compose down && docker-compose --profile flower up
```

Note: The Flower UI will be available at `http://localhost:5555`
