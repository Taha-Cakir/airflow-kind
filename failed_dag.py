from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 4, 27),
}

dag = DAG('failed_dag', default_args=default_args, schedule_interval=None)

task1 = BashOperator(
    task_id='task1',
    bash_command='echo "This is task 1"',
    dag=dag
)

task2 = BashOperator(
    task_id='task2',
    bash_command='exit 1',
    dag=dag
)

task1 >> task2
