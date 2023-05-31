from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
import os
import pandas as pd

# Funções
def created_folders():
    # Variavel responsável pos capiturar o path raiz do projeto
    path_folder = os.getcwd() 

    """data_dir = os.path.join(path_folder, 'data')
    os.chmod(data_dir, 0o777)
    print(f"Permissões do diretório pai 'data' alteradas para 777.")"""

    # Abrindo e carregando o arquivo CSV com os nomes das pastas que serão criadas para o projeto
    file_path = os.path.join(path_folder, 'dags/nome_diretorios.csv')
    f = pd.read_csv(file_path)
    lista_folders = f['Folders'].to_list()

    # Laço for percorre a lista das partas cridas e inicia as pastas do projeto
    for i in lista_folders:

        # Verifica se as pastas já foram criadas, se não, as cria.
        if not os.path.exists(path_folder + '/data/' + i):
            os.makedirs(path_folder + '/data/' + i)
            print(f"Diretório {i} criado com sucesso!")
        else:
            print(f"O diretório {i} já existe.")


dag_owner = 'olist_brasil'

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

    created_folders_task = PythonOperator(
        task_id='created_folders_task',
        python_callable=created_folders,
        provide_context=True
    )

created_folders_task 