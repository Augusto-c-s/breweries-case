from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from src.data.bronze_layer import bronze_layer
from src.data.silver_layer import silver_layer
from src.data.gold_layer import gold_layer
from src.utils.api_client import fetch_breweries_data

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}
dag = DAG(
    'pipeline',
    default_args=default_args,
    description='Pipeline to use api and create the',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2023, 11, 1),
    catchup=False,
)

def fetch_and_save_bronze():
    data = fetch_breweries_data()
    bronze_layer(data)

fetch_data_task = PythonOperator(
    task_id='fetch_data_from_api',
    python_callable=fetch_and_save_bronze,
    dag=dag,
)

transform_silver_task = PythonOperator(
    task_id='transform_bronze_to_silver',
    python_callable=silver_layer,
    dag=dag,
)

create_gold_task = PythonOperator(
    task_id='create_gold_layer',
    python_callable=gold_layer,
    dag=dag,
)

fetch_data_task >> transform_silver_task >> create_gold_task
