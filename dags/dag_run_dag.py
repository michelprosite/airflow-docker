from airflow import DAG
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from airflow.operators.bash import BashOperator
from datetime import datetime


dag_owner = 'dag_run_dag'

with DAG(dag_id=dag_owner,
         description='',
         start_date=datetime(2021, 12, 1),
         schedule_interval='30 * * * *',
         catchup=False) as dag:

    task1 = BashOperator(
        task_id='task1',
        bash_command='echo "Task 1"'
    )

    task2 = TriggerDagRunOperator(
        task_id='task2',
        trigger_dag_id="outradag"
    )

    task1 >> task2
