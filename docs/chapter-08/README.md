# Scraping Data from Githubs to Postgres

## 1. Create a new DAGs

Create a `github_to_postgres.py` file in the `dags` folder.

## 2. Create a new Connection for HTTP

1. Admin -> Connections -> Create a new record
2. Connection Type: `HTTP`
3. Conn Id: `http`
4. Host: `api.github.com`
5. Schema: `https`
6. Save

## 3. Add SimpleHTTPOperator to the DAG

Add following code to the `github_to_postgres.py` file and Test the DAG.

```python
import json
from datetime import datetime

from airflow import DAG
from airflow.providers.http.operators.http import SimpleHttpOperator

with DAG('github_to_postgres', start_date=datetime(2024, 1, 1), catchup=False) as dag:
    extract_user = SimpleHttpOperator(
        task_id='extract_github_user',
        method='GET',
        http_conn_id='http',
        endpoint='users/JakeWharton',
        log_response=True,
        do_xcom_push=True,
        response_filter=lambda response: json.loads(response.text)
    )

    extract_user
```

## 4. Add Postgres Connection

1. Admin -> Connections -> Create a new record
2. Connection Type: `Postgres`
3. Conn Id: `postgres`
4. Host: `postgres`
5. Port: `5432`
6. Username: `airflow`
7. Password: `airflow`
8. Database: `airflow`

## 5. Add PostgresOperator to Create Table

Add following code to the `github_to_postgres.py` file and Test the DAG.

Run and Test the DAG.

Note: You can expose port `5432` to connect to the Postgres container.

```python
import json
from datetime import datetime

from airflow import DAG
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator

with DAG('github_to_postgres', start_date=datetime(2024, 1, 1), catchup=False) as dag:

    ...

    create_user_table = PostgresOperator(
        task_id="create_github_users_table",
        postgres_conn_id="postgres",
        sql="""
                CREATE TABLE IF NOT EXISTS github_users (
                id SERIAL PRIMARY KEY,
                name VARCHAR NOT NULL,
                avatar_url VARCHAR NOT NULL
                )
              """,
    )

    extract_user >> create_user_table
```

## 6. Add PostgresOperator to Insert Data

Add following code to the `github_to_postgres.py` file and Test the DAG.

```python

import json
from datetime import datetime

from airflow import DAG
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator

with DAG('github_to_postgres', start_date=datetime(2024, 1, 1), catchup=False) as dag:
    ...

    insert_user = PostgresOperator(
        task_id="insert_github_user",
        postgres_conn_id="postgres",
        sql="""
            INSERT INTO github_users (name, avatar_url)
            VALUES (
                '{{ task_instance.xcom_pull(task_ids='extract_github_user')['name'] }}',
                '{{ task_instance.xcom_pull(task_ids='extract_github_user')['avatar_url'] }}'
            )
        """
    )


    extract_user >> create_user_table >> insert_user
```

[Back to Root](../../README.md)
[Go Next](../chapter-09/README.md)
