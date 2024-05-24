# What's Airflow?

Apache Airflow is Workflow Orchestration, It allows you to program, schedule, and monitor workflows

## What's a Workflow Orchestration?

Workflow Orchestration is the process of triggering and monitoring the status of tasks; nothing more, nothing less.

<img src="orchestrate.jpeg" width="60%">

## Data Pipelines

Process of moving data from one place to another, it can be transforming data, loading data, etc.

Example 1: Source -> Destination

```mermaid {"id":"01HYFVGQBKQ6VAZ0AYGX4Y9CF8"}
graph LR
    A[Source] --> B[Destination]
```

## ETL - Extract, Transform, Load

### Single Source

```mermaid {"id":"01HYFVGQBKQ6VAZ0AYH06G28QC"}
graph LR
    A[Extract] --> B[Transform] --> C[Load]
```

### Multiple Sources

```mermaid {"id":"01HYFVGQBKQ6VAZ0AYH3FDT2PX"}
graph LR
    A[SharePoint] --> B[Transform] --> C[GCS]
    D[Google Drive] --> B
```

## ELT - Extract, Load, Transform

```mermaid
graph LR
    A[Extract] --> B[Load]
    B --> C[Transform]
```

## Reverse ETL

Moving data from destination to source

## Data Stack

### ETL - Extract, Transform, Load

#### EL - Extract, Load

- Fivetran
- Stitch
- Airbyte

#### T - Transform

- dbt
- Currently, some of Data Warehouses tools can do transformations

## What's Airflow? (Again)

Airflow is `Workflow` Orchestration, specifically designed tp batch-oriented workflows.

We can use Airflow to `create, schedule, and monitor any workflows.`

**Automate Workflows, Trigger Scripts, Schedule, etc.**

Program wrokflows in Python, schedule them, and monitor them.

<img src="dags.png" width="80%">

## Workflow as Code

Allow you to define your workflows as code, which makes it easy to version control, test, and deploy.

```python {"id":"01HYB7G78163BYDKA2K9JA8PCQ"}
from datetime import datetime

from airflow import DAG
from airflow.decorators import task
from airflow.operators.bash import BashOperator

# A DAG represents a workflow, a collection of tasks
with DAG(dag_id="demo", start_date=datetime(2022, 1, 1), schedule="0 0 * * *") as dag:
    # Tasks are represented as operators
    hello = BashOperator(task_id="hello", bash_command="echo hello")

    @task()
    def airflow():
        print("airflow")

    # Set dependencies between tasks
    hello >> airflow()
```

## Airflow Use Cases

<img src="./usecase.png" width="90%">

## When to use Airflow?

1. Ability to implement pipelines using `Python` code
2. Airflow community has already developed a rich collection of extensions that allow Airflow to integrate with many different types of databases, cloud services, and so on
3. Rich `scheduling semantics` allow you to run your pipelines at specific times, regular intervals, or in response to events
4. Backfilling capabilities allow you to `run historical jobs`
5. `Web interface` provides an easy way to monitor result of your pipelines

## When not to use Airflow?

1. Airflow is `not designed for real-time processing, it is batch-oriented`
2. Highly dynamic pipelines, which added/removed tasks between every pipelines run
3. Little or no Python experience


## Summary

- **Airbyte**: Soliving Data Integration
- **Airflow**: Solving Scheduling
- **dbt**: Solving Data Transformations

[Back to Root](../../README.md)
[Go Next](../chapter-02/README.md)
