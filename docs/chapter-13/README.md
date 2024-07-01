# Celery Executor (Local)

## What is (Airflow)Executor?

Executors are the mechanism by which `task instances` get run.

### Executors in Airflow

Local Executors

- Local Executor
- Sequential Executor

Remote Executors

- CeleryExecutor
- CeleryKubernetesExecutor
- KubernetesExecutor
- KubernetesLocalExecutor

## Celery Executor - Example for Local

1. Looking at the `docker-compose.yaml` file, we can see that the default executor is `CeleryExecutor`.
2. Enable `flower` UI via `docker compose up -d flower`.
3. Access the `flower` UI via `http://localhost:5555`.
4. We'll see the `celery` workers and the `celery` queues.
