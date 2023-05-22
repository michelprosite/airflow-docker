from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

# Nome da DAG
dag_owner = 'defaultargs'

default_args = {
    'depends_on_past': False,
    'start_date': datetime(2023, 3, 5),
    'email': ['test@test.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(seconds=10)
}

with DAG(dag_id=dag_owner,
         default_args=default_args,
         description='',
         start_date=datetime(2021, 12, 1),
         schedule_interval='30 * * * *',
         default_view='graph',
         tags=['processo', 'tag', 'pipeline'],
         catchup=False) as dag:

    task1 = BashOperator(
        task_id='task1',
        bash_command='echo "Task 1"'
    )

    task2 = BashOperator(
        task_id='task2',
        bash_command='echo "Task 2"'
    )

    task3 = BashOperator(
        task_id='task3',
        bash_command='echo "Task 3"'
    )

    task1 >> task2 >> task3
