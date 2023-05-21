from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime
from airflow.utils.task_group import TaskGroup

dag_owner = 'daggroup'

with DAG(dag_id=dag_owner,
         description='',
         start_date=datetime(2021, 12, 1),
         schedule_interval='30 * * * *',
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


    task4 = BashOperator(
            task_id='task4',
            bash_command='echo "Task 4"'
        )


    task5 = BashOperator(
            task_id='task5',
            bash_command='echo "Task 5"'
        )


    task6 = BashOperator(
            task_id='task6',
            bash_command='echo "Task 6"'
        )

    tsk_group1 = TaskGroup("tsk_group1")

    task7 = BashOperator(
            task_id='task7',
            bash_command='echo "Task 7"',
            task_group = tsk_group1
        )


    task8 = BashOperator(
            task_id='task8',
            bash_command='echo "Task 8"',
            task_group = tsk_group1
        )

    task9 = BashOperator(
        task_id='task9',
        bash_command='echo "Task 9"',
        trigger_rule='all_failed',
        task_group = tsk_group1
    )

    task1 >> task2
    task3 >> task4
    [task2, task4] >> task5 >> task6
    task6 >> tsk_group1
