from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
import os

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
    bash_command_download = (
        "r= !pwd; "
        "PATH_FOLDER= $r[0] + '/transient'; "
        "os.environ['PATH_FOLDER']= PATH_FOLDER; "
        "cd $PATH_FOLDER && kaggle datasets download -d olistbr/brazilian-ecommerce; "
        "cd $PATH_FOLDER && unzip brazilian-ecommerce.zip; "
        "cd $PATH_FOLDER && rm -r brazilian-ecommerce.zip"
    )
    return bash_command_download

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
