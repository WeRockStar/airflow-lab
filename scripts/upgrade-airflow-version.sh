#!/bin/bash

read -p "Enter Airflow version (ex. 2.10.2): " airflow_version

pattern="2.10.4"

working_directory="./"

find "$working_directory" -type f \( -name "*.yaml" -o -name "*.yml" \) -exec sed -i "" "s/$pattern/$airflow_version/g" {} \;

echo "✅ DONE: $airflow_version is replaced in all yaml files."
