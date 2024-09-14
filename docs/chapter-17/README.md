# Airflow on Kubernetes

Learn how to running Airflow on Kubernetes, use Helm and Kind to deploy Airflow on Kubernetes Cluster.

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Kind](https://kind.sigs.k8s.io/docs/user/quick-start/)
- [Helm](https://helm.sh/docs/intro/install/)
- [Kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
- [k9s](https://k9scli.io/topics/install/) (Optional)

## Kubernetes Cluster

- Create a Kubernetes Cluster using Kind

```bash
kind create cluster --name airflow-cluster --config kind-cluster.yaml
```

- Ensure K8s Context

```bash
kubectl cluster-info --context kind-airflow-cluster

# view current context
kubectl config current-context
```

## Helm for Airflow

- Add Airflow Helm Repository

```bash
helm repo add apache-airflow https://airflow.apache.org

# or update the repo
helm repo update
```

- Install Airflow using Helm

```bash
helm install airflow apache-airflow/airflow
```

Helm will show the following output:

```console
NAME: airflow
LAST DEPLOYED: Sat Sep 14 16:34:00 2024
NAMESPACE: default
STATUS: deployed
REVISION: 1
TEST SUITE: None
NOTES:
Thank you for installing Apache Airflow 2.9.3!

Your release is named airflow.
You can now access your dashboard(s) by executing the following command(s) and visiting the corresponding port at localhost in your browser:

Airflow Webserver:     kubectl port-forward svc/airflow-webserver 8080:8080 --namespace default
Default Webserver (Airflow UI) Login credentials:
    username: admin
    password: admin
Default Postgres connection credentials:
    username: postgres
    password: postgres
    port: 5432

You can get Fernet Key value by running the following:

    echo Fernet Key: $(kubectl get secret --namespace default airflow-fernet-key -o jsonpath="{.data.fernet-key}" | base64 --decode)

###########################################################
#  WARNING: You should set a static webserver secret key  #
###########################################################

You are using a dynamically generated webserver secret key, which can lead to
unnecessary restarts of your Airflow components.

Information on how to set a static webserver secret key can be found here:
https://airflow.apache.org/docs/helm-chart/stable/production-guide.html#webserver-secret-key
```
