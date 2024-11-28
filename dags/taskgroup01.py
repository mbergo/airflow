from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.email import EmailOperator
from airflow.utils.task_group import TaskGroup
from datetime import datetime

dag = DAG('TaskGroupDag01', description="task group", schedule_interval=None, start_date=datetime(2024,11,27), catchup=False)

task_group = TaskGroup("task_group", dag=dag)
task1 = BashOperator(task_id="tsk1",bash_command="sleep 5", dag=dag)
task2 = BashOperator(task_id="tsk2",bash_command="sleep 5", dag=dag)
task3 = BashOperator(task_id="tsk3",bash_command="sleep 5", dag=dag, trigger_rule="all_failed")
task4 = BashOperator(task_id="tsk4",bash_command="sleep 5", dag=dag)
task5 = BashOperator(task_id="tsk5",bash_command="sleep 5", dag=dag)
task6 = BashOperator(task_id="tsk6",bash_command="exit 1", dag=dag)
task7 = BashOperator(task_id="tsk7",bash_command="sleep 5", dag=dag, task_group=task_group)
task8 = BashOperator(task_id="tsk8",bash_command="sleep 5", dag=dag, task_group=task_group)
task9 = BashOperator(task_id="tsk9",bash_command="sleep 5", dag=dag, task_group=task_group)

# precedence
task1 >> task2
task3 >> task4
[task2, task4] >> task5 >> task6 >> task_group