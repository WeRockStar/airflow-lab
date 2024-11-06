FROM apache/airflow:2.10.3-python3.12 AS build

ENV DEBIAN_FRONTEND=noninteractive \
    PIP_DEFAULT_TIMEOUT=100 \
    # Allow statements and log messages to immediately appear
    PYTHONUNBUFFERED=1 \
    # disable a pip version check to reduce run-time & log-spam
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    # cache is useless in docker image, so disable to reduce image size
    PIP_NO_CACHE_DIR=1 \
    # opt out of running pip as the 'root' user warning
    PIP_ROOT_USER_ACTION=ignore \
    POETRY_VERSION=1.8.2

WORKDIR /tmp
COPY pyproject.toml poetry.lock ./

RUN pip install "poetry==${POETRY_VERSION}"
RUN set -ex \
    poetry install --no-root --no-ansi --no-interaction --without dev --with prod\
    && poetry export -f requirements.txt -o requirements.txt

# final state
FROM apache/airflow:2.10.3-python3.12 AS final

ENV DEBIAN_FRONTEND=noninteractive \
    PIP_DEFAULT_TIMEOUT=100 \
    # Allow statements and log messages to immediately appear
    PYTHONUNBUFFERED=1 \
    # disable a pip version check to reduce run-time & log-spam
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    # cache is useless in docker image, so disable to reduce image size
    PIP_NO_CACHE_DIR=1 \
    # opt out of running pip as the 'root' user warning
    PIP_ROOT_USER_ACTION=ignore

WORKDIR /tmp
COPY --from=build /tmp/requirements.txt .

RUN pip install -r /tmp/requirements.txt

USER 50000
