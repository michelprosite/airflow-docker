from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
import os
import pandas as pd
from kaggle.api.kaggle_api_extended import KaggleApi

# Funções
diretorio = "/opt/airflow/data/transient"

def verifica_arquivos(diretorio):    
    arquivos = os.listdir(diretorio)
    if len(arquivos) == 0:
        print("O diretório está vazio.")
        return False
    else:
        print("O diretório contém arquivos.")
        return True

def downloads_folders(ti):
    # Defina o caminho para o arquivo da chave de API
    api_key_path = '/home/michel/airflow-docker/.kaggle/kaggle.json'

    # Altere as permissões do arquivo da chave de API
    os.chmod(api_key_path, 0o600)

    # Configurar a biblioteca Kaggle
    api = KaggleApi()
    api.authenticate()

    # Definir o caminho da pasta
    current_dir = os.getcwd()
    path_folder = "/home/michel/airflow-docker/data/transient"

    # Criar a pasta se ela não existir
    os.makedirs(path_folder, exist_ok=True)

    # Definir o caminho completo do arquivo
    file_path = os.path.join(path_folder, 'brazilian-olist-ecommerce.zip')

    # Fazer o download do conjunto de dados
    api.dataset_download_files('michelsouzasantana/brazilian-olist-ecommerce', path=path_folder, unzip=True)

    # Remover o arquivo zip
    #os.remove(file_path)

def e_valida(ti):
    validador = ti.xcom_pull(task_ids='verifica_arquivos_task')
    if validador:
        return 'downloads_folders_task'
    else:
        return 'arquivos_existentes'


dag_owner = 'captura_dados'

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
         description='Criando os diretórios do projeto.',
         start_date=datetime(2023, 5, 27),
         schedule_interval=None,
         default_view='graph',
         catchup=False) as dag:

    verifica_arquivos_task = PythonOperator(
        task_id='verifica_arquivos_task',
        python_callable=verifica_arquivos,
        op_kwargs={'diretorio': diretorio}
    )

    downloads_folders_task = PythonOperator(
        task_id='downloads_folders_task',
        python_callable=downloads_folders,
        provide_context=True
    )

    e_valida_task = BranchPythonOperator(
        task_id='e_valida',
        python_callable=e_valida,
        provide_context=True
    )

    arquivos_existentes_task = BashOperator(
        task_id='arquivos_existentes',
        bash_command='echo "Quantidade não OK"'
    )

verifica_arquivos_task >> e_valida_task >> [downloads_folders_task, arquivos_existentes_task]
