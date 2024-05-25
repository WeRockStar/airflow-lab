# Google Drive to GCS

## 1. Create Service Account on GCP

- Create a service account on GCP
- Sharing
- Download the JSON key file

## 2. Prepare Image on Google Drive

- Upload the image to Google Drive
- Share access to the service account email
- Copy Drive folder ID

## 3. Create Connection on Airflow

1. Admin -> Connections -> Create a new record
2. Conn Id: `gcp`
3. Connection Type: `Google Cloud`
4. Project Id: `<your-project-id>`
5. Keyfile Path: `/path/to/your/keyfile.json` or Keyfile JSON
6. Scope: `https://www.googleapis.com/auth/cloud-platform, https://www.googleapis.com/auth/drive.readonly`
7. Save the connection
8. Optional: Test the connection (need to enable)

## 4. Create a new DAGs

Create a `drive_to_gcs.py` file in the `dags` folder

```python {"id":"01HYJTRDQNECJNF4J3RK22P38Q"}
from airflow import DAG
from datetime import datetime

with DAG('drive_to_gcs', start_date=datetime(2024, 5, 1),
         schedule_interval='@daily',
         tags=["XXXX"],
         catchup=False) as dag:
         pass
```

## 5. Add GoogleDriveToGCSOperator

```python {"id":"01HYJTRDQNECJNF4J3RP90ZS24"}
from airflow import DAG
from datetime import datetime

from airflow.providers.google.cloud.transfers.gdrive_to_gcs import GoogleDriveToGCSOperator

with DAG('drive_to_gcs', start_date=datetime(2024, 5, 1),
         schedule_interval='@daily',
         tags=["XXX"],
         catchup=False) as dag:
         
    sync_drive_to_gcs = GoogleDriveToGCSOperator(
        task_id='sync_drive_to_gcs',
        gcp_conn_id='gcp',
        folder_id='1p7Ymz5CVDwANgHMBdD4Q4bgOel0Kn0Ec',
        file_name='helm.png',
        bucket_name='<BUCKET_NAME>',
        object_name='helm.png'
    )

    sync_drive_to_gcs
```

## 6. Test the DAG

[Back to Root](../../README.md)
[Go Next](../chapter-07/README.md)