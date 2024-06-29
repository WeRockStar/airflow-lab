# Working with Airflow Sensor

Sensor is a special type of operator that will keep running until a certain criterion is met.

<img src="./po.png" width="55%">

## 1. Create a New DAGs

Create  a `sensor.py` python file in the `dags` folder

## 2. Copy Python Code

Copy code from `drive_to_gcs.py` and paste it in the `sensor.py` file

```python {"id":"01HYPZPMPBC5SCV84XCCV3EE6G"}
from airflow import DAG
from datetime import datetime

from airflow.providers.google.cloud.transfers.gdrive_to_gcs import GoogleDriveToGCSOperator

# Change DAGs ID drive_to_gcs to sensor
with DAG('drive_to_gcs', start_date=datetime(2024, 5, 1),
         schedule_interval='@daily',
         tags=["XXXX"],
         catchup=False) as dag:

    sync_drive_to_gcs = GoogleDriveToGCSOperator(
        task_id='sync_drive_to_gcs',
        gcp_conn_id='gcp',
        folder_id='<FOLDER_ID>',
        file_name='helm.png',
        bucket_name='<BUCKET_NAME>',
        object_name='helm.png'
    )

    sync_drive_to_gcs
```

## 3. Modify DAGs ID

Change the DAGs ID to `sensor`

```python {"id":"01HYPZPMPBC5SCV84XCFREC3DV"}
with DAG('sensor', start_date=datetime(2024, 5, 1),
         schedule_interval='@daily',
         tags=["XXXX"],
         catchup=False) as dag:
```

## 4. Add a Sensor Operator

Add a `GoogleDriveFileSensor` operator to the DAGs

```python {"id":"01HYPZPMPBC5SCV84XCH9QD707"}

from airflow.providers.google.suite.sensors.drive import GoogleDriveFileExistenceSensor

...
detect_file = GoogleDriveFileExistenceSensor(
    task_id='detect_file',
    gcp_conn_id='gcp',
    folder_id='<FOLDER_ID>',
    file_name='helm.png'
)

```

## 5. Set Task Dependencies

Set the task dependencies on Graph View

```python {"id":"01HYPZPMPBC5SCV84XCJR8SXP9"}

detect_file >> sync_drive_to_gcs

```

[Back to Root](../../README.md)
[Go Next](../chapter-08/README.md)
