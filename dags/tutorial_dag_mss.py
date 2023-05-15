from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime
import pandas as pd
import requests
import json

dag_owner = 'tutorial_dag_mss'


def captura_conta_dados():
    url = "https://data.cityofnewyork.us/resource/rc75-m7u3.json"
    response = requests.get(url)
    df = pd.DataFrame(json.loads(response.content))
    qtd = len(df.index)
    return qtd


def e_valida(ti):
    qtd = ti.xcom_pull(task_ids = 'capitura_conta_dados')
    if qtd is None:
        qtd = 0

    if (qtd >= 1000):
        return 'valido'
    return 'nvalido'


with DAG(dag_id=dag_owner,
         description='',
         start_date=datetime(2021, 12, 1),
         schedule_interval='30 * * * *',
         catchup=False,
         )as dag:

    captura_conta_dados = PythonOperator(
        task_id=dag_owner,
        python_callable=captura_conta_dados
    )


    e_valida = BranchPythonOperator(
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

captura_conta_dados >> e_valida >> [valido, nvalido]
