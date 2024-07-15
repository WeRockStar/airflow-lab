# Overview of Airflow

## Airflow Components

- **Web Server**: The Web Server is the **UI for Airflow**. provides a UI to manage DAGs and the Airflow environment.
- **Scheduler**: The Scheduler is the core of Airflow. It **triggers** tasks and manages their dependencies. The Scheduler chooses how to prioritize the running and execution of tasks within the system.
- **Executor**: The Executor is the mechanism by which `task instances` get run. The concept of an executor is a pluggable component of Airflow. Airflow comes with many executors out of the box and you can also provide your own.
- **Metadata Database**: The Metadata Database is the **persistent store** for metadata related to the state of workflows and tasks in Airflow. The database, often referred to as the metadata database, also stores credentials, connections, history, and configuration.
- **DAGs (Directed Acyclic Graphs)**: A DAG is a **collection of all the tasks** you want to run, organized in a way that **reflects their relationships and dependencies**. A DAG’s definition is written in Python files that are placed in Airflow’s DAG_FOLDER.

## DAGs (Directed Acyclic Graphs)

### Pipeline as Graph

- **Nodes**: Tasks
- **Edges**: Dependencies

```mermaid
graph LR;
    A[Task1] --- B[Task2]
    B --- C[Task3]
    C --- D[Task4]
```

### Directed Graphs

- **Directed**: Edges have a direction

```mermaid
graph LR;
    A[Task1] --> B[Task2]
    B --> C[Task3]
    C --> D[Task4]
```

### Directed Acyclic Graphs (DAGs) ✅

- **Acyclic**: No cycles

```mermaid
graph LR;
    A[Task1] --> B[Task2]
    B --> C[Task3]
    B --> D[Task4]
    C --> E[Task5]
    D --> E
```

### Not DAGs ❌

```mermaid
graph LR;
    A[Task1] --> B[Task2]
    B --> C[Task3]
    C --> A
```

### Mai Mee DAG (aka. แดก)

<img src="./meme.jpeg" width="65%" alt="meme for DAGs">

## Start Airflow

```bash
dokcker compose up -d
# dags folder is mounted to the container

# start lightweight Airflow
docker compose -f docker-compose.light.yml up -d
```

## Access the Airflow UI

[http://localhost:8080](http://localhost:8080)

```yaml
username: airflow
password: airflow
```

- Overview of DAGs on the Airflow UI
- Pause/Unpause DAGs
- `example-complex` DAG
- Trigger a DAG
- View the Graph View of a DAG
- Recent Tasks
- Workflow/DAGs Status
- Calendar View
- Logging

## Airflow Concepts

- **Task**: A task is a parameterized instance of an Operator. It describes a single task in a workflow.
- **Operator**: An Operator is `a class that acts as a template for carrying out some work`. Most Operators require a DAG object in their constructor. The DAG defines the task and the dependencies between tasks.

[Back to Root](../../README.md)
[Go Next](../chapter-03/README.md)
