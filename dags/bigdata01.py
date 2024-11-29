from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime
from plugins.big_data_operator import BigDataOperator

dag = DAG('bigdata01', description="big data", schedule_interval=None, start_date=datetime(2024,11,27), catchup=False)

big_data = BigDataOperator(task_id="tsk1", path_to_csv_file="/tmp/data.csv", path_to_save_file="/tmp/data.parquet", file_type='parquet', dag=dag)

big_data