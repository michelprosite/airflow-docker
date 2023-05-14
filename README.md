# airflow-docker
## Michel Souza Santana
> 14/05/2023
*****

### Iniciando o airflow

michel@mss:~/airflow-docker$ docker-compose up airflow-init

WARNING: The AIRFLOW_UID variable is not set. Defaulting to a blank string.
Creating network "airflow-docker_default" with the default driver
Creating volume "airflow-docker_postgres-db-volume" with default driver
Pulling postgres (postgres:13)...
13: Pulling from library/postgres
9e3ea8720c6d: Already exists
7782b3e1be4b: Already exists
247ec4ff783a: Already exists
f7ead6900700: Already exists
e7afdbe9a191: Already exists
3ef71fe7cece: Already exists
1459ebb56be5: Already exists
3595124f6861: Already exists
21d1b00b8369: Already exists
aa0f5cff9b82: Already exists
ac773378c58e: Already exists
9f6cf64ad0b2: Already exists
64705da81f0c: Already exists
Digest: sha256:ce2086148580daf694c72ced7e1f452d5dd46e9118c9273a29e2343b3289a4ef
Status: Downloaded newer image for postgres:13
Pulling redis (redis:latest)...
latest: Pulling from library/redis
9e3ea8720c6d: Already exists
7bb0a593ef8e: Pull complete
1563ab48b627: Pull complete
e71aa54519a0: Pull complete
e43bffb29bfd: Pull complete
a8fb6ae3ba1b: Pull complete

### Subindo o airflow no docker

michel@mss:~/airflow-docker$ docker-compose up 

WARNING: The AIRFLOW_UID variable is not set. Defaulting to a blank string.
airflow-docker_postgres_1 is up-to-date
airflow-docker_redis_1 is up-to-date
Starting airflow-docker_airflow-init_1 ... done
airflow-docker_airflow-scheduler_1 is up-to-date
airflow-docker_airflow-webserver_1 is up-to-date
Attaching to airflow-docker_postgres_1, airflow-docker_redis_1, airflow-docker_airflow-init_1, airflow-docker_airflow-scheduler_1, airflow-docker_airflow-webserver_1
airflow-init_1       | /home/airflow/.local/lib/python3.7/site-packages/airflow/configuration.py:367: FutureWarning: The auth_backends setting in [api] has had airflow.api.auth.backend.session added in the running config, which is needed by the UI. Please update your config before Apache Airflow 3.0.
airflow-init_1       |   FutureWarning,
airflow-init_1       | 
airflow-init_1       | WARNING!!!: AIRFLOW_UID not set!
airflow-init_1       | If you are on Linux, you SHOULD follow the instructions below to set 
airflow-init_1       | AIRFLOW_UID environment variable, otherwise files will be owned by root.
airflow-init_1       | For other operating systems you can get rid of the warning with manually created .env file:
airflow-init_1       |     See: https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html#setting-the-right-airflow-user
airflow-init_1       | 
airflow-init_1       | The container is run as root user. For security, consider using a regular user account.
airflow-init_1       | 
airflow-init_1       | /home/airflow/.local/lib/python3.7/site-packages/airflow/configuration.py:367: FutureWarning: The auth_backends setting in [api] has had airflow.api.auth.backend.session added in the running config, which is needed by the UI. Please update your config before Apache Airflow 3.0.
airflow-init_1       |   FutureWarning,
airflow-init_1       | DB: postgresql+psycopg2://airflow:***@postgres/airflow
airflow-init_1       | Performing upgrade with database postgresql+psycopg2://airflow:***@postgres/airflow
airflow-init_1       | [2023-05-14 23:22:34,936] {migration.py:204} INFO - Context impl PostgresqlImpl.
airflow-init_1       | [2023-05-14 23:22:34,937] {migration.py:211} INFO - Will assume transactional DDL.
airflow-init_1       | [2023-05-14 23:22:34,952] {db.py:1530} INFO - Creating tables
airflow-init_1       | INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
airflow-init_1       | INFO  [alembic.runtime.migration] Will assume transactional DDL.
airflow-init_1       | Upgrades done
airflow-init_1       | /home/airflow/.local/lib/python3.7/site-packages/airflow/configuration.py:367: FutureWarning: The auth_backends setting in [api] has had airflow.api.auth.backend.session added in the running config, which is needed by the UI. Please update your config before Apache Airflow 3.0.
airflow-init_1       |   FutureWarning,
airflow-scheduler_1  | 
airflow-scheduler_1  | /home/airflow/.local/lib/python3.7/site-packages/airflow/configuration.py:367: FutureWarning: The auth_backends setting in [api] has had airflow.api.auth.backend.session added in the running config, which is needed by the UI. Please update your config before Apache Airflow 3.0.
airflow-scheduler_1  |   FutureWarning,
airflow-scheduler_1  | /home/airflow/.local/lib/python3.7/site-packages/airflow/configuration.py:367: FutureWarning: The auth_backends setting in [api] has had airflow.api.auth.backend.session added in the running config, which is needed by the UI. Please update your config before Apache Airflow 3.0.
airflow-scheduler_1  |   FutureWarning,
airflow-scheduler_1  |   ____________       _____________
airflow-scheduler_1  |  ____    |__( )_________  __/__  /________      __
airflow-scheduler_1  | ____  /| |_  /__  ___/_  /_ __  /_  __ \_ | /| / /
airflow-scheduler_1  | ___  ___ |  / _  /   _  __/ _  / / /_/ /_ |/ |/ /
airflow-scheduler_1  |  _/_/  |_/_/  /_/    /_/    /_/  \____/____/|__/
airflow-scheduler_1  | [2023-05-14 23:22:18,378] {scheduler_job.py:701} INFO - Starting the scheduler
airflow-scheduler_1  | [2023-05-14 23:22:18 +0000] [31] [INFO] Starting gunicorn 20.1.0
airflow-scheduler_1  | [2023-05-14 23:22:18,379] {scheduler_job.py:706} INFO - Processing each file at most -1 times
airflow-scheduler_1  | [2023-05-14 23:22:18 +0000] [31] [INFO] Listening at: http://0.0.0.0:8793 (31)
airflow-scheduler_1  | [2023-05-14 23:22:18 +0000] [31] [INFO] Using worker: sync
airflow-scheduler_1  | [2023-05-14 23:22:18 +0000] [32] [INFO] Booting worker with pid: 32
airflow-scheduler_1  | [2023-05-14 23:22:18 +0000] [33] [INFO] Booting worker with pid: 33
airflow-scheduler_1  | [2023-05-14 23:22:18,409] {executor_loader.py:107} INFO - Loaded executor: LocalExecutor
airflow-scheduler_1  | [2023-05-14 23:22:18,657] {manager.py:163} INFO - Launched DagFileProcessorManager with pid: 135
airflow-scheduler_1  | [2023-05-14 23:22:18,658] {scheduler_job.py:1369} INFO - Resetting orphaned tasks for active dag runs
airflow-scheduler_1  | [2023-05-14 23:22:18,778] {settings.py:58} INFO - Configured default timezone Timezone('UTC')


### Finalizando o container docker-airflow

michel@mss:~/airflow-docker$ docker-compose down

WARNING: The AIRFLOW_UID variable is not set. Defaulting to a blank string.
Stopping airflow-docker_airflow-webserver_1 ... done
Stopping airflow-docker_airflow-scheduler_1 ... done
Stopping airflow-docker_postgres_1          ... done
Stopping airflow-docker_redis_1             ... done
Removing airflow-docker_airflow-webserver_1 ... done
Removing airflow-docker_airflow-scheduler_1 ... done
Removing airflow-docker_airflow-init_1      ... done
Removing airflow-docker_postgres_1          ... done
Removing airflow-docker_redis_1             ... done
Removing network airflow-docker_default
