from airflow import DAG
from airflow.operators.bash import BashOperator
# from airflow.operators.email import EmailOperator
from datetime import datetime
from airflow.operators.trigger_dagrun import TriggerDagRunOperator


dag = DAG('dag_run_dag', description="dag call dag", schedule_interval=None, start_date=datetime(2024,11,27), catchup=False)

task1 = BashOperator(task_id="tsk1",bash_command="sleep 5", dag=dag)
task2 = TriggerDagRunOperator(task_id="dag02_called", trigger_dag_id="dag02_called", dag=dag)
# task2 = BashOperator(task_id="tsk2",bash_command="sleep 5", dag=dag)
# task3 = BashOperator(task_id="tsk3",bash_command="sleep 5", dag=dag)
# task4 = BashOperator(task_id="tsk4",bash_command="sleep 5", dag=dag)
# task5 = BashOperator(task_id="tsk5",bash_command="sleep 5", dag=dag)
# task6 = BashOperator(task_id="tsk6",bash_command="exit 1", dag=dag)
# task7 = BashOperator(task_id="tsk7",bash_command="sleep 5", dag=dag)
# task8 = BashOperator(task_id="tsk8",bash_command="sleep 5", dag=dag)
# task9 = BashOperator(task_id="tsk9",bash_command="sleep 5", dag=dag)

# # precedence
# tasking = [task7, task8, task9]
# task1 >> task2
# task3 >> task4
# [task2, task4] >> task5 >> task6 >> tasking
# precedence
task1 >> task2