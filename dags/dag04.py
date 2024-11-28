from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG('fourth_dag', description="our fourth dag", schedule_interval=None, start_date=datetime(2024,11,27), catchup=False) as dag:

    task1 = BashOperator(task_id="tsk1",bash_command="sleep 10", dag=dag)
    task2 = BashOperator(task_id="tsk2",bash_command="sleep 10", dag=dag)
    task3 = BashOperator(task_id="tsk3",bash_command="sleep 10", dag=dag)

    # precedence
    # [task1, task2] >> task3

    task1.set_upstream(task2)
    task2.set_upstream(task3)