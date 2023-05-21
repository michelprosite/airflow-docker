from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime
import pandas as pd
import requests
import json

dag_owner = 'primeiradag'


def captura_conta_dados():
    url = "https://data.cityofnewyork.us/resource/rc75-m7u3.json"
    response = requests.get(url)
    df = pd.DataFrame(json.loads(response.content))
    qtd = len(df.index)
    return qtd


def e_valida(ti):
    qtd = ti.xcom_pull(task_ids='captura_conta_dados_task')
    if qtd is None:
        qtd = 0

    if qtd >= 1000:
        return 'valido'
    return 'nvalido'


with DAG(dag_id=dag_owner,
         description='',
         start_date=datetime(2021, 12, 1),
         schedule_interval='30 * * * *',
         catchup=False) as dag:

    captura_conta_dados_task = PythonOperator(
        task_id='captura_conta_dados_task',
        python_callable=captura_conta_dados
    )

    e_valida_task = BranchPythonOperator(
        task_id='e_valida',
        python_callable=e_valida
    )

    valido = BashOperator(
        task_id='valido',
        bash_command='echo "Quantidade OK"'
    )

    nvalido = BashOperator(
        task_id='nvalido',
        bash_command='echo "Quantidade não OK"'
    )

    task1 = BashOperator(
        task_id='task1',
        bash_command='echo "Task 1"'
    )

    task2 = BashOperator(
        task_id='task2',
        bash_command='echo "Task 2"'
    )

    captura_conta_dados_task >> e_valida_task >> [valido, nvalido]
    valido >> task1
    nvalido >> task2
