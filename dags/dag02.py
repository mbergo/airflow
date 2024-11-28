from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

dag = DAG('second_dag', description="our second dag", schedule_interval=None, start_date=datetime(2024,11,27), catchup=False)

task1 = BashOperator(task_id="tsk1",bash_command="sleep 10", dag=dag)
task2 = BashOperator(task_id="tsk2",bash_command="sleep 10", dag=dag)
task3 = BashOperator(task_id="tsk3",bash_command="sleep 10", dag=dag)

# precedence
task1 >> [task2, task3]
